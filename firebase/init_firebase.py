import firebase_admin
from firebase_admin import credentials
import dotenv
import os
dotenv.load_dotenv()

def initialize_firebase():
    # Path to your service account JSON file
    cred = credentials.Certificate('firebase-credential.json')

    return(firebase_admin.initialize_app(cred))


firebase_app = initialize_firebase()

def firebase_app_module():
   return firebase_app