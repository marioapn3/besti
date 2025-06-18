# import os
# import logging
# from pathlib import Path
# from typing import List
# import torch
# from PIL import Image
# # import clip
# # from sklearn.metrics.pairwise import cosine_similarity
# from fastapi import APIRouter, UploadFile, HTTPException, status, Form
# from fastapi.responses import JSONResponse
# import shutil

# # Konfigurasi dan variabel global
# DATASET_PATH = os.getenv("DATASET_PATH", "public/batik_dataset")
# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
# BATIK_KEYWORDS = [
#     'cendrawasih', 'tambal', 'sogan', 'sidomukti', 'sidoluhur', 'sekar', 'priangan',
#     'pekalongan', 'parang', 'megamendung', 'lasem', 'keraton', 'kawung', 'gentongan',
#     'garutan', 'ciamis', 'ceplok', 'celup', 'betawi', 'bali'
# ]

# model = None
# preprocess = None
# dataset_features = {}
# dataset_image_paths = {}

# logger = logging.getLogger(__name__)

# router = APIRouter()

# # def load_clip_model():
# #     """Memuat model CLIP dan preprocess transform."""
# #     global model, preprocess
# #     try:
# #         model, preprocess = clip.load("ViT-B/32", device=DEVICE)
# #         logger.info("CLIP model loaded successfully.")
# #     except Exception as e:
# #         logger.error(f"Failed to load CLIP model: {e}")
# #         raise RuntimeError("Could not load CLIP model.")

# def encode_image(image: Image.Image) -> torch.Tensor:
#     """Mengkodekan gambar menjadi fitur menggunakan CLIP."""
#     image = preprocess(image).unsqueeze(0).to(DEVICE)
#     with torch.no_grad():
#         image_features = model.encode_image(image)
#     return image_features

# def load_dataset():
#     """Memuat dan mengkodekan gambar dataset saat startup."""
#     dataset_path = Path(DATASET_PATH)
#     if not dataset_path.exists():
#         logger.error("Dataset path does not exist.")
#         raise RuntimeError("Dataset path does not exist.")

#     for keyword in BATIK_KEYWORDS:
#         motif_folder = dataset_path / f"batik-{keyword.lower()}"
#         if motif_folder.is_dir():
#             dataset_features[keyword] = []
#             dataset_image_paths[keyword] = []
#             for image_path in motif_folder.glob("*.jpg"):
#                 try:
#                     image = Image.open(image_path).convert("RGB")
#                     features = encode_image(image)
#                     dataset_features[keyword].append(features)
#                     dataset_image_paths[keyword].append(str(image_path))
#                 except Exception as e:
#                     logger.warning(f"Failed to process image {image_path}: {e}")
#             logger.info(f"Loaded {len(dataset_features[keyword])} images for motif {keyword}")

# def evaluate_similarity(input_features: torch.Tensor, motif_features: List[torch.Tensor]) -> float:
#     """Menghitung similarity tertinggi antara input dan dataset."""
#     if not motif_features:
#         return 0.0
#     similarities = [
#         cosine_similarity(
#             input_features.cpu().numpy(),
#             motif.cpu().numpy()
#         )[0][0]
#         for motif in motif_features
#     ]
#     return max(similarities) if similarities else 0.0

# def recognize_batik_image(image: Image.Image, motif_name: str) -> dict:
#     """
#     Recognize batik motif from an image and compare it with the specified motif.
    
#     Args:
#         image: PIL Image object
#         motif_name: Name of the batik motif to compare against
        
#     Returns:
#         dict: Recognition results containing motif name and similarity score
        
#     Raises:
#         ValueError: If motif_name is invalid
#         RuntimeError: If no dataset images found for the motif
#     """
#     # Validasi motif_name
#     motif_name = motif_name.lower()
#     if motif_name not in BATIK_KEYWORDS:
#         raise ValueError(f"Invalid motif name. Must be one of: {', '.join(BATIK_KEYWORDS)}")

#     # Encode input image
#     input_features = encode_image(image)

#     # Evaluasi similarity
#     motif_features = dataset_features.get(motif_name, [])
#     if not motif_features:
#         raise RuntimeError(f"No dataset images found for motif '{motif_name}'.")

#     similarity_score = evaluate_similarity(input_features, motif_features)

#     return {
#         "similarity_score": float(similarity_score),
#     }  

# @router.post("/recognize-batik/")
# async def recognize_batik(file: UploadFile, motif_name: str = Form(...)):
#     """Endpoint untuk mengenali motif batik dari gambar yang diunggah dan motif name via form-data."""
#     if not file.content_type.startswith("image/"):
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File must be an image.")

#     temp_file_path = f"temp_{file.filename}"
#     try:
#         # Simpan file sementara
#         with open(temp_file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)

#         # Baca dan proses gambar
#         image = Image.open(temp_file_path).convert("RGB")
        
#         # Gunakan fungsi recognize_batik_image
#         result = recognize_batik_image(image, motif_name)
#         return JSONResponse(content=result)

#     except ValueError as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
#     except RuntimeError as e:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
#     except Exception as e:
#         logger.error(f"Error processing request: {e}")
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
#     finally:
#         # Bersihkan file sementara
#         if os.path.exists(temp_file_path):
#             os.remove(temp_file_path)
