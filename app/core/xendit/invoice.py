import time
import xendit
from xendit.apis import InvoiceApi
from xendit.invoice.model.create_invoice_request import CreateInvoiceRequest
from pprint import pprint
from app.core.config import settings
from loguru import logger

# Set the Xendit API key
xendit.set_api_key(settings.XENDIT_API_KEY)

def xendit_invoice(external_id, amount, payer_email, description):
    """
    Create an invoice using Xendit's API and return the invoice URL.
    
    :param external_id: A unique external ID for the invoice.
    :param amount: The amount for the invoice.
    :param payer_email: The payer's email address.
    :param description: A description for the invoice.
    :return: The URL for the created invoice, or None if an error occurs.
    """
    try:
        # Create an instance of the API client and the InvoiceApi
        api_client = xendit.ApiClient()
        api_instance = InvoiceApi(api_client)
        
        # Set up the request body for creating the invoice
        create_invoice_request = CreateInvoiceRequest(
            external_id=external_id,
            amount=amount,
            payer_email=payer_email,
            description=description,
            success_redirect_url=settings.PAYMENT_SUCCESS_REDIRECT_URL,
            failure_redirect_url=settings.PAYMENT_FAILURE_REDIRECT_URL,
        )

        # Create the invoice using the Xendit API
        api_response = api_instance.create_invoice(create_invoice_request)

        # Return the invoice URL from the API response
        return api_response.invoice_url
    except xendit.XenditSdkException as e:
        logger.error(f"Error creating Xendit invoice: {e}")
        return None