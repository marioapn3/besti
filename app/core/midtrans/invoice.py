import requests
from app.core.config import settings
import base64
from loguru import logger
def midtrans_invoice(id, amount, payer_email, description):
    """
    Create an invoice using Midtrans's API and return the invoice URL.
    
    :param id: A unique external ID for the invoice.
    :param amount: The amount for the invoice.
    :param payer_email: The payer's email address.
    :param description: A description for the invoice.
    :return: The URL for the created invoice, or None if an error occurs.
    """
    try:
        # Set the Midtrans API key
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {base64.b64encode(f'{settings.MIDTRANS_SERVER_KEY}:'.encode()).decode()}"
        }
        
        # Set up the request body for creating the invoice
        payload = {
            "transaction_details": {
                "order_id": id,
                "gross_amount": amount
            },
             "item_details": [{
                "id": "ITEM1",
                "price": amount,
                "quantity": 1,
                "name": description,
            }],
            "credit_card": { "secure": True },
            "callbacks": {
                "finish": settings.PAYMENT_SUCCESS_REDIRECT_URL,
            },
        }

        # Create the invoice using the Midtrans API
        response = requests.post(settings.MIDTRANS_URL, json=payload, headers=headers)
        json = response.json()
        url = json.get("redirect_url")
        return url
    except Exception as e:
        logger.error(f"Exception when calling Midtrans API: {e}")
        return None