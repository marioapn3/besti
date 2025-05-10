import requests
from app.core.config import settings
import anthropic
from loguru import logger
import json
class ClaudeService:

    @classmethod
    def _make_api_request(cls, system_message, messages, max_tokens=1000, temperature=0.5, top_p=1, top_k=40):
        """
        Fungsi internal untuk mengirim permintaan ke API Perplexity.
        """
        response = anthropic.Anthropic(
            api_key=settings.CLAUDE_API_KEY,
        ).messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=8192,
            system=system_message,
            messages=messages,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
        )

        response_json = response.json()
        return response_json
    
    @classmethod
    def _make_api_request_v2(cls, system_message, messages, max_tokens=1000, temperature=0.5, top_p=1, top_k=40):
        """
        Fungsi internal untuk mengirim permintaan ke API Perplexity.
        """
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": settings.CLAUDE_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        data = {
            "model": "claude-3-7-sonnet-20250219",
            "max_tokens": 8192,
            "messages": messages,
            "system": system_message,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
        

    @staticmethod
    def _build_message(content, role="system"):
        """
        Fungsi untuk membangun format pesan.
        """
        return {"content": content, "role": role}
    """
    Make Contract
    """
    @classmethod
    def make_contract(cls , text: str):
        system_message = "Anda adalah system untuk membuat extract informasi sesuai dengan permintaan user, dan response dalam format JSON."
        user_message =f"""Extract important information (
                            'location_name' as string,
                            'location_address' as string,
                            'start_date' as datetime in format %Y-%m-%d,
                            'end_date' as datetime in format %Y-%m-%d,
                            'cooperation_type' fixed cost lease or revenue share as string,
                            'payment_terms' payment period monthly, quarterly, yearly, etc as string,
                            'monthly_cost_amount' in total amount or revenue share percentage as string,
                            'security_deposit_amount' as string,
                            'last_invoice_due' as datetime in format %Y-%m-%d,
                            'last_invoice_amount' as string,
                            'document_date' as datetime in format %Y-%m-%d,
                            'document_type' agreement or invoice as string,
                            and 'additional_info' as single level json
                        ) from this lease agreement and put it in json format: {text}"""

        return cls._make_api_request_v2(
            system_message=system_message,
            messages=[
                cls._build_message(user_message, role="user"),
            ]
        )
    """
    MakeConclusion
    """
    @classmethod
    def make_conclusion(cls , data: dict):
        """
        Memetakan data invoice ke customer.
        """
        system_message = """
            Anda adalah system yang digunakan untuk memberikan kesimpulan dari sebuah chat yang berisi 
            tentang pembahasan sebuah Hukum dan Perundang-undangan di Indonesia.
            Dari chat yang saya berikan, saya ingin system memberikan response berupa json dengan contoh :
            {
                "title": "Judul Kesimpulan dari chat yang diberikan"
                "category" : "Pilih antara 4 kategori (Hukum Pidana, Hukum Pajak, Hukum Lalu Lintas, Hukum Perdata)"
                "body" : "Isi dari kesimpulan yang diberikan"
                "uu_reference" : [
                    "list pasal uu referensi", "list pasal uu referensi", "list pasal uu referensi"
                ]
                "keyword" : "berikan 1 kata kunci dari kesimpulan yang diberikan (contoh: Tilang Elektronik, KUHP Baru 2023, Hak Cipta Digital dll)"
            }
            Hanya response dalam format JSON. ATRIBUT JSON HARUS SESUAI DENGAN YANG SAYA BERIKAN CONTOHNYA.
        """
        user_message = f"""
            Ini adalah history chat yang harus diolah 
            <context>{data}</context>
            Hanya response dalam format JSON. ATRIBUT JSON HARUS SESUAI DENGAN YANG SAYA BERIKAN CONTOHNYA.
        """

        return cls._make_api_request_v2(
            system_message=system_message,
            messages=[
                cls._build_message(user_message, role="user"),
            ]
        )
    """
    ExtractDocument
    """
    @classmethod
    def extract_document(cls , data: dict):
        """
        Memetakan data invoice ke customer.
        """
        system_message = """
            You are a system to mapping my invoices to the right customer.
            Map extracted text to predefined fields (e.g., Invoice Number, Date, Total).
            I need to extract the invoice number, date, total amount and all of the field from the invoice.
            I want the response in JSON format like : 
                    
            "fields": { // Extracted fields
                "invoice_number": {
                "value": "INV2024/0001",
                "confidence": (confidence score)
            },
            "date": {   
                "value": "2024-10-22",
                "confidence": (confidence score)
            },
            "due_date": {
                "value": "2024-10-22",
                "confidence": (confidence score)
            },
            "total": {
                "value": 9230.77,
                "confidence": (confidence score)
                }
            }, and other important data from the invoice.

            ONLY RESPONSE THIS MESSAGE IN JSON FORMAT. DONT RESPONSE THIS MESSAGE IN TEXT FORMAT.
        """
        user_message = f"""
            Ini adalah data yang harus diolah {data}.
            ONLY RESPONSE THIS MESSAGE IN JSON FORMAT. DONT RESPONSE THIS MESSAGE IN TEXT FORMAT.
        """

        messages = [
            cls._build_message(system_message, role="system"),
            cls._build_message(user_message, role="user"),
        ]
        return cls._make_api_request(messages)


    @classmethod
    def map_invoice(cls, data: str):
        """
        Memetakan data invoice ke customer.
        """
        system_message = """
            You are a system to mapping my invoices to the right customer.
            Map extracted text to predefined fields (e.g., Invoice Number, Date, Total).
            ONLY RESPONSE THIS MESSAGE IN JSON FORMAT.
        """
        user_message = f"ini adalah datanya : {data}"

        messages = [
            cls._build_message(system_message, role="system"),
            cls._build_message(user_message, role="user"),
        ]
        return cls._make_api_request(messages)

    @classmethod
    def get_insight(cls, data: dict, question: str):
        """
        Memberikan wawasan dari data invoice.
        """
        system_message = """
            You are a system to giving insight about data in invoices to the right customer.
            Answer the question based on the data in the invoice. Answer the question in text format.
        """
        user_message = f"This is invoice data: {data}, and the question is: {question}"

        messages = [
            cls._build_message(system_message, role="system"),
            cls._build_message(user_message, role="user"),
        ]
        return cls._make_api_request(messages)

    @classmethod
    def generate_dataset(cls, prompt: str, rows: int, temperature: float, top_p: float = 0.9, top_k: int = 40):
        """
        Menghasilkan dataset dari input pengguna.
        """
        system_message = """
            You are the system to generate dataset from users input.
            ONLY RESPONSE THIS MESSAGE IN JSON FORMAT.
            I want the response in JSON format like:
            {
                "employees" (type of dataset): [
                    {
                        "first_name": "John",
                        "last_name": "Doe",
                        "age": 30,
                        "city": "New York"
                    },
                    .....
                ]
            }
        """
        user_message = f"This is the prompt: {prompt}\nI want to generate total {rows} rows of dataset based on the prompt above. ONLY RESPONSE THIS MESSAGE IN JSON FORMAT."

        messages = [
            cls._build_message(user_message, role="user"),
        ]
        return cls._make_api_request(system_message,messages, temperature=temperature, top_p=top_p, top_k=top_k, max_tokens=5000)

    @classmethod
    def navigator(cls, data: dict, question: str, temperature: float = 0.5, top_p: float = 1, top_k: int = 40):
        """
        Memberikan wawasan berbasis data dengan format JSON.
        """
        system_message = """
            To enable users to interact with AI insights by selecting specific data sources 
            (e.g., invoices, sales data, or customer feedback), 
            generating a default AI-powered report, and customizing the report to their needs.
            You are a system to giving insight about data in invoices to the right customer.
            Response with json format. For example, if the user wants the report in chart form, 
            you can respond with:
                {
                    "summary": "Your invoice data shows 5 overdue payments totaling $10,000.",
                    "chart": {                            
                        "type": "line",
                        "data": [
                            {"month": "Jan", "value": 4000},
                            ...
                        ]
                    }
                }
            ONLY RESPONSE THIS MESSAGE IN JSON FORMAT. DON'T RESPONSE THIS MESSAGE IN TEXT FORMAT.
        """
        user_message = f"""
                    This is sources data: {str(data)}, and the question is: {question}.
                    ONLY RESPONSE THIS MESSAGE IN JSON FORMAT.
                    DON'T RESPONSE THIS MESSAGE IN TEXT FORMAT.

                    I WANT JSON FORMAT RESPONSE LIKE:
                    - summary
                    - chart (if needed) with type "line" or "bar" and relevant data.
                """

        messages = [
            cls._build_message(system_message, role="system"),
            cls._build_message(user_message, role="user"),
        ]
        return cls._make_api_request(messages, max_tokens= 10000, temperature=temperature, top_p=top_p, top_k=top_k)

