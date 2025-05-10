import requests
from app.core.config import settings
import json
from loguru import logger


def perplexity_service(data: str) :
    url = settings.URL_PERPLEXITY

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "content": """
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
                 """,
                "role": "system"
            },
            {
                "content": "ini adalah datanya : " + data + "ONLY RESPONSE THIS MESSAGE IN JSON FORMAT. DONT RESPONSE THIS MESSAGE IN TEXT FORMAT.", 
                "role": "user"
            }
        ],
        "max_tokens": 1000,
        "return_images": False,
        "temperature": 0.5,
        # "frequency_penalty": 0,
        # "presence_penalty": 0,
        # "top_p": 1
    }

    headers = {
        "Authorization": f"Bearer {settings.PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.post(url, json=payload, headers=headers)
    
    # Parse the JSON response
    response_json = response.json()
    
    # Check if the response contains 'choices' and extract the content
    if 'choices' in response_json and len(response_json['choices']) > 0:
        content = response_json['choices'][0]['message']['content']
        # logger.info("Content from Perplexity : " + content)
        # return json.loads(content)
        return content
    else:
        logger.error("No choices in the response.")
        return None



def insight_invoice(data: dict, question: str) :
    url = settings.URL_PERPLEXITY

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "content": """
                    You are a system to giving insight about data in invoices to the right customer.
                    Answer the question based on the data in the invoice. Answer the question in text format.
                 """,
                "role": "system"
            },
            {
                "content": "This is invoice data : " + str(data) + ", and the question is : " + question,
                "role": "user"
            }
        ],
        "max_tokens": 1000,
        "return_images": False,
        "temperature": 0.5,
    }

    headers = {
        "Authorization": f"Bearer {settings.PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    response_json = response.json()
    
    if 'choices' in response_json and len(response_json['choices']) > 0:
        content = response_json['choices'][0]['message']['content']
        return content
    else:
        logger.error("No choices in the response.")
        return None




def dataset_generation(prompt: str,rows: int, temperature: float, top_p: float = 0.9 , top_k: int = 40) :
    url = settings.URL_PERPLEXITY

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "content": """
                    You are the system to generate dataset from users input.
                    ONLY RESPONSE THIS MESSAGE IN JSON FORMAT. DONT RESPONSE THIS MESSAGE IN TEXT FORMAT.
                 """,
                "role": "system"
            },
            {
                "content": """
                    This is the prompt : """ + prompt + """

                    I want to generate total """ + str(rows) + """ rows of dataset based on the prompt above.

                    Response this message only the dataset in JSON format.
                """,
                "role": "user"
            }
        ],
        "max_tokens": 5000,
        "return_images": False,
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k
    }

    headers = {
        "Authorization": f"Bearer {settings.PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.post(url, json=payload, headers=headers)
    
    # Parse the JSON response
    response_json = response.json()
    
    # Check if the response contains 'choices' and extract the content
    if 'choices' in response_json and len(response_json['choices']) > 0:
        content = response_json['choices'][0]['message']['content']
        return content
    else:
        logger.error("No choices in the response.")
        return None



def navigator(data: dict, question: str, temperature: float = 0.5 , top_p: float = 1, top_k: int = 40) :
    url = settings.URL_PERPLEXITY

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "content": """
                    To enable users to interact with AI insights by selecting specific data sources (e.g., invoices, sales data, or customer feedback), generating a default AI-powered report, and customizing the report to their needs.
                    You are a system to giving insight about data in invoices to the right customer.
                    Response with json format. For example, if the user wants the report in chart form, you can respond with:
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
                 """,
                "role": "system"
            },
            {
               "content": f"""
                    This is sources data: {str(data)}, and the question is: {question}.
                    ONLY RESPONSE THIS MESSAGE IN JSON FORMAT.
                    DON'T RESPONSE THIS MESSAGE IN TEXT FORMAT.

                    I WANT JSON FORMAT RESPONSE LIKE:
                    - summary
                    - chart (if needed) with type "line" or "bar" and relevant data.
                 """,
                "role": "user"
            }
        ],
        "max_tokens": 1000,
        "return_images": False,
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        # "frequency_penalty": 0,
        # "presence_penalty": 0,
        # "top_p": 1
    }

    headers = {
        "Authorization": f"Bearer {settings.PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    response_json = response.json()
    
    if 'choices' in response_json and len(response_json['choices']) > 0:
        content = response_json['choices'][0]['message']['content']
        return content , response_json['usage']['total_tokens']
    else:
        logger.error("No choices in the response.")
        return None

