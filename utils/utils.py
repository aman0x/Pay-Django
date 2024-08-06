import requests
from django.conf import settings

TWO_FACTOR_API_KEY = settings.TWO_FACTOR_API_KEY
TWO_FACTOR_API_URL = "https://2factor.in/API/V1"

def send_otp(phone):
    url = f"{TWO_FACTOR_API_URL}/{TWO_FACTOR_API_KEY}/SMS/{phone}/AUTOGEN"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def verify_otp(session_id, otp):
    url = f"{TWO_FACTOR_API_URL}/{TWO_FACTOR_API_KEY}/SMS/VERIFY/{session_id}/{otp}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
