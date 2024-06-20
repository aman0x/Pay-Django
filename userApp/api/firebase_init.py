import firebase_admin
from firebase_admin import credentials
import os

firebase_app = None

def initialize_firebase():
    global firebase_app
    if not firebase_app:
        cred_path = os.path.join(os.path.dirname(__file__), "../../paymorz/firebase-config.json")
        cred = credentials.Certificate(cred_path)
        firebase_app = firebase_admin.initialize_app(cred)

initialize_firebase()
