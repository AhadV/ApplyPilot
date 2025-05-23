import firebase_admin
from firebase_admin import credentials, firestore, storage
import os

key_path = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(key_path)
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'applypilot-d9a35.firebasestorage.app'  # <-- REPLACE this with your actual Firebase bucket if different
    })

db = firestore.client()
