import firebase_admin
from firebase_admin import storage
import uuid

bucket = storage.bucket()

def upload_resume_file(file_data: bytes, filename: str, content_type: str) -> str:
    unique_filename = f"{uuid.uuid4()}_{filename}"
    blob = bucket.blob(f"resumes/{unique_filename}")
    blob.upload_from_string(file_data, content_type=content_type)
    blob.make_public()  # Optional: Use token-based URLs instead if needed
    return blob.public_url
