import requests
from app.core.config import settings


class PerplexityService:
    API_URL = settings.URL_PERPLEXITY
    API_KEY = settings.PERPLEXITY_API_KEY

    @classmethod
    def _make_api_request(cls, messages, max_tokens=1000, temperature=0.5, top_p=1, top_k=40):
        """
        Fungsi internal untuk mengirim permintaan ke API Perplexity.
        """
        payload = {
            "model": "sonar",
            "messages": messages,
            "max_tokens": max_tokens,
            "return_images": False,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }

        headers = {
            "Authorization": f"Bearer {cls.API_KEY}",
            "Content-Type": "application/json",
        }

        response = requests.post(cls.API_URL, json=payload, headers=headers)
        response_json = response.json()

        if 'choices' in response_json and len(response_json['choices']) > 0:
            content = response_json['choices'][0]['message']['content']
            return content, response_json.get('usage', {}).get('total_tokens', None)
        else:
            logger.error("No choices in the response.")
            return None, None

    @staticmethod
    def _build_message(content, role="system"):
        """
        Fungsi untuk membangun format pesan.
        """
        return {"content": content, "role": role}

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
            cls._build_message(system_message, role="system"),
            cls._build_message(user_message, role="user"),
        ]
        return cls._make_api_request(messages, temperature=temperature, top_p=top_p, top_k=top_k, max_tokens=5000)

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

