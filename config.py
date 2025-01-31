import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_key'
    API_LINK = 'https://order.drcash.sh/v1/order'
    API_HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer RLPUUOQAMIKSAB2PSGUECA'
    }
