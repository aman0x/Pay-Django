import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('firebase.py')
firebase_admin.initialize_app(cred)