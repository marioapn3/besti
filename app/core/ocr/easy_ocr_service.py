import easyocr
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import docx
import os

class EasyOCRService:
    def __init__(self, languages=None):
        """
        Initialize EasyOCR service.
        :param languages: List of languages for OCR (default: ['en', 'id']).
        """
        if languages is None:
            languages = ['id', 'en']
        self.reader = easyocr.Reader(languages)

    def extract_text(self, file_path):
        """
        Extract text from a DOC, TXT, PDF, or image file using EasyOCR.
        :param file_path: Path to the file (DOC, TXT, PDF, or image).
        :return: Extracted text as a string.
        """
        file_extension = os.path.splitext(file_path)[1].lower()

        try:
            if file_extension == '.pdf':
                # Handle PDF files
                return self._extract_text_from_pdf(file_path)
            elif file_extension == '.txt':
                # Handle TXT files
                return self._extract_text_from_txt(file_path)
            elif file_extension in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
                # Handle Image files (JPG, PNG, etc.)
                return self._extract_text_from_image(file_path)
            elif file_extension == '.docx':
                # Handle DOCX files
                return self._extract_text_from_docx(file_path)
            else:
                return f"Unsupported file type: {file_extension}"

        except Exception as e:
            return f"Error processing file: {e}"

    def _extract_text_from_pdf(self, file_path):
        """Extract text from a PDF file using EasyOCR."""
        images = convert_from_path(file_path)
        extracted_text = ""
        for image in images:
            image_np = np.array(image)
            text = self.reader.readtext(image_np, detail=0)
            extracted_text += " ".join(text) + "\n"
        return extracted_text.strip()

    def _extract_text_from_txt(self, file_path):
        """Extract text from a TXT file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()

    def _extract_text_from_image(self, file_path):
        """Extract text from an image file using EasyOCR."""
        image = Image.open(file_path)
        image_np = np.array(image)
        text = self.reader.readtext(image_np, detail=0)
        return " ".join(text)

    def _extract_text_from_docx(self, file_path):
        """Extract text from a DOCX file."""
        doc = docx.Document(file_path)
        extracted_text = ""
        for para in doc.paragraphs:
            extracted_text += para.text + "\n"
        return extracted_text.strip()
