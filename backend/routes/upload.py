from fastapi import APIRouter, File, UploadFile, Form
from firebase.firebase_init import db
from services.upload import upload_resume_file

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(user_id: str = Form(...), file: UploadFile = File(...)):
    file_data = await file.read()
    file_url = upload_resume_file(file_data, file.filename, file.content_type)

    # Save the URL to Firestore under the user
    db.collection("users").document(user_id).set({
        "resume_url": file_url
    }, merge=True)

    return {"resume_url": file_url}
