import json
import re
import logging

logger = logging.getLogger(__name__)

def clean_extracted_response(raw_response):
    try:
        logger.debug(f"Raw response before cleaning: {raw_response}")  # Debug raw response

        # Step 1: Remove single-line comments (// ...)
        cleaned_response = re.sub(r"//.*?$", "", raw_response, flags=re.MULTILINE).strip()

        # Step 2: Remove JSON code block markers (```json and ```)
        cleaned_response = cleaned_response.replace("```json", "").replace("```", "").strip()

        # Step 3: Handle multi-line comments (/* ... */) if necessary
        cleaned_response = re.sub(r"/\*.*?\*/", "", cleaned_response, flags=re.DOTALL).strip()

        logger.debug(f"Cleaned response before JSON parsing: {cleaned_response}")  # Debug cleaned response

        # Step 4: Parse the cleaned response into JSON
        return json.loads(cleaned_response, strict=False)

    except json.JSONDecodeError as e:
        logger.error(f"JSON Decode Error: {e}. Problematic response: {cleaned_response}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}. Raw response: {raw_response}")
    return None

