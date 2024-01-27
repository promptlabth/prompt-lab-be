import firebase_admin
from firebase_admin import credentials, auth, App, delete_app
from firebase_admin.credentials import Certificate

class FirebaseService:

    firebase_app: App
    cerd: credentials.Certificate

    def __init__(self) -> None:
        self.cerd = credentials.Certificate('firebase-credential.json')
        
    
    def validate(self, token: str):
        self.firebase_app = firebase_admin.initialize_app(self.cerd, name="firebase_prompts")
        try:
            data = auth.verify_id_token(
            id_token=token,
            app=self.firebase_app
            )
        except Exception as e:
            print(e)
            data = None
        self.finish() # Call after end of process
        return data
    
    def finish(self):
        delete_app(self.firebase_app)