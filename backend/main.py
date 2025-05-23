from fastapi import FastAPI
from routes import preferences
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env for OpenAI key

app = FastAPI()

app.include_router(preferences.router)

