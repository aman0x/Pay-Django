import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

TWO_FACTOR_API_KEY = settings.TWO_FACTOR_API_KEY
TWO_FACTOR_API_URL = "https://2factor.in/API/V1"

def send_otp(phone, template_name=None):
    url = f"{TWO_FACTOR_API_URL}/{TWO_FACTOR_API_KEY}/SMS/{phone}/AUTOGEN"
    if template_name:
        #url += f"?template_name={template_name}"
        url += f"?template_name=OTP for Login"
    try:
        response = requests.get(url)
        response_data = response.json()
        if response.status_code == 200 and response_data.get('Status') == 'Success':
            return response_data
        else:
            logger.error(f"Failed to send OTP: {response_data}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Request to 2Factor API failed: {e}")
        return None

def verify_otp(session_id, otp):
    url = f"{TWO_FACTOR_API_URL}/{TWO_FACTOR_API_KEY}/SMS/VERIFY/{session_id}/{otp}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
