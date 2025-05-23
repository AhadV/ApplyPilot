from fastapi import APIRouter
from models import Preferences
from firebase.firebase_init import db

router = APIRouter()

@router.post("/set-preferences")
def set_preferences(prefs: Preferences):
    db.collection("users").document(prefs.user_id).set({
        "preferences": prefs.dict()
    }, merge=True)
    return {"status": "preferences saved"}

