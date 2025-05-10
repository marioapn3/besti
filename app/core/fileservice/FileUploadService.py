import os
from datetime import datetime
from fastapi import UploadFile
from typing import Tuple

class FileUploadService:
    UPLOAD_DIR = './private/sources/'
    LP_DIR = './private/legal_purse/'
    LP_CONTRACT = './private/contract/'
    ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx', '.txt']
    ALLOWED_MIME_TYPES = [
        'image/jpeg', 
        'image/png', 
        'application/pdf', 
        'application/msword', 
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 
        'text/plain'
    ]

    @staticmethod
    def create_upload_directory(organisation_id: str) -> str:
        customer_folder = os.path.join(FileUploadService.UPLOAD_DIR, organisation_id)
        os.makedirs(customer_folder, exist_ok=True)
        return customer_folder

    def create_lp_dir() -> str:
        folder = os.path.join(FileUploadService.LP_DIR)
        os.makedirs(folder, exist_ok=True)
        return folder
    

    def create_contract_dir() -> str:
        folder = os.path.join(FileUploadService.LP_CONTRACT)
        os.makedirs(folder, exist_ok=True)
        return folder


    @staticmethod
    def validate_file(file: UploadFile) -> None:
        file_extension = os.path.splitext(file.filename)[1].lower()
        if file_extension not in FileUploadService.ALLOWED_EXTENSIONS:
            raise ValueError("file_extension_not_allowed")
        if file.content_type not in FileUploadService.ALLOWED_MIME_TYPES:
            raise ValueError("file_mime_type_not_allowed")

    @staticmethod
    async def save_file(file: UploadFile, folder_path: str) -> Tuple[str, str]:
        timestamp = datetime.utcnow().isoformat().replace(":", "-").replace(".", "-")
        safe_file_name = f"{os.path.splitext(file.filename)[0]}_{timestamp}{os.path.splitext(file.filename)[1]}"
        file_location = os.path.join(folder_path, safe_file_name)

        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)

        return file_location, safe_file_name
