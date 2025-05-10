from fastapi.responses import JSONResponse
from fastapi import status

def generate_paginated_response(name_eng: str, name_indo:str,data: list, total: int, page: int, limit: int) -> dict:
    """
    Generate a standard paginated response.
    :param data: List of data items.
    :param total: Total number of items in the collection.
    :param page: Current page number.
    :param limit: Number of items per page.
    :param process_time: Processing time in seconds.
    :return: A dictionary representing the paginated response.
    """
    total_pages = (total + limit - 1) // limit  
    return {
        "response_code": 200,
        "success": True,
        "message": {
            "ID": f"Daftar {name_indo} berhasil ditemukan",
            "EN": f"{name_eng} List retrieved successfully"
        },
        "data": data,
        "pagination": {
            "total": total,
            "page": page,
            "limit": limit,
            "total_pages": total_pages
        },
    }


def generate_response(data: dict | None, message: dict, success: bool = True, status_code: int = 200) -> dict:
    """
    Generate a standard JSON response.
    :param data: The response data.
    :param message: The response message.
    :param success: Whether the request was successful.
    :param status_code: The HTTP status code.
    :return: A dictionary representing the JSON response.
    """
    return JSONResponse(status_code=status_code, content={
        "response_code": status_code,
        "success": success,
        "message": message,
        "data": data  
    })

def generate_response_error(error: dict, status_code: int = 400) -> dict:
    """
    Generate a standard JSON response for an error.
    :param error: The error message.
    :param status_code: The HTTP status code.
    :return: A dictionary representing the JSON response.
    """
    return JSONResponse(status_code=status_code, content=error)

