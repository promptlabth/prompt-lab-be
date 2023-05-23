import firebase_admin
from firebase_admin import credentials
def initialize_firebase():
    # Path to your service account JSON file
    cred = credentials.Certificate('prompt-lab-383408-firebase-adminsdk-i24ml-e58c5bd2ad.json')
    return(firebase_admin.initialize_app(cred))


firebase_app = initialize_firebase()

def firebase_app_module():
   return firebase_app