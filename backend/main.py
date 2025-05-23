from fastapi import FastAPI
from routes import preferences, upload
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Include all routes
app.include_router(preferences.router)
app.include_router(upload.router)
