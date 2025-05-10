from fastapi import FastAPI, File, UploadFile, HTTPException, Form

import uvicorn
from PIL import Image
import io
import time
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import APIRouter

from .recognize_handler import recognize_batik_image


# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

router = APIRouter()

def generate_caption(image, tema):
    """Generate caption using Gemini"""
    try:
        # Initialize Gemini Pro Vision model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate caption
        response = model.generate_content([
            """
            Anda adalah seorang ahli seni batik.
            Anda akan memberikan sebuah feedback terhadap gambar batik dari user untuk penilaian.
            Kriteria penilaian:
            - Tema => Temanya adalah """ + tema + """
            - Keunikan Motif
            - Teknik Pewarnaan dan komposisi -> Edge detection + color harmony analysis.

            Return dalam format JSON dengan key:
            tema : string (apakah gambar sesuai dengan tema berikan penjelasan nya )
            keunikan_motif : string (apakah motif gambar unik dan menarik berikan penjelasan nya)
            teknik_pewarnaan_dan_komposisi : string (apakah teknik pewarnaan dan komposisi gambar baik (Edge Detection + Color Harmony Analysis) dan menarik berikan penjelasan nya)
            kesimpulan : string (kesimpulan dari penilaian diatas)
        """,
            image
        ])
        
        # Clean and parse the response text as JSON
        try:
            # Remove markdown code block formatting
            response_text = response.text
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            # Parse the cleaned JSON string
            response_json = json.loads(response_text)
            return response_json
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=500, detail=f"Invalid JSON response from Gemini: {str(e)}")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating caption: {str(e)}")

@router.post("/caption")
async def create_caption(
    file: UploadFile = File(...),
    tema: str = Form(...)
):
    """
    Endpoint untuk generate caption dari gambar
    
    Parameters:
    - file: File gambar yang akan diproses (JPEG, PNG, dll)
    - tema: Tema batik yang akan dinilai
    
    Returns:
    - status: Status response
    - caption: Caption yang dihasilkan
    - rating: Rating yang dihasilkan
    - feedback: Feedback yang dihasilkan
    - processing_time: Waktu yang dibutuhkan untuk memproses
    """
    try:
        # Validasi file
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File harus berupa gambar")
        
        # Baca file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Generate caption
        start_time = time.time()
        response_data = generate_caption(image, tema)
        processing_time = time.time() - start_time

        # Recognize batik image
        start_time = time.time()
        similiarity_score = recognize_batik_image(image, tema)
        processing_time = time.time() - start_time
        
        return {
            "status": "success",
            "feedback" : {
                   "tema": response_data.get("tema", ""),
                "keunikan_motif": response_data.get("keunikan_motif", ""),
                "teknik_pewarnaan_dan_komposisi": response_data.get("teknik_pewarnaan_dan_komposisi", ""),
                "kesimpulan": response_data.get("kesimpulan", ""),
            },
            "similiarity_score": similiarity_score.get("similarity_score", ""),
            "processing_time": f"{processing_time:.2f} seconds",
            "filename": file.filename,
            "tema": tema
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def root():
    """Endpoint untuk mengecek status API"""
    return {
        "status": "active",
        "message": "Image Captioning API is running",
        "endpoints": {
            "POST /caption": "Generate caption from image",
            "GET /": "API status check"
        }
    }

if __name__ == "__main__":
    uvicorn.run("api:router", host="0.0.0.0", port=8000, reload=True) 