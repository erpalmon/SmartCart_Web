# backend/firebase_config.py
import firebase_admin # type: ignore
from firebase_admin import credentials, auth # type: ignore

# Only initialize once
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")  
    firebase_admin.initialize_app(cred)
