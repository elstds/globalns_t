import requests

from config import Config

def send_querry(phone, name):
    data = {
        'stream_code': 'vv4uf',
        'client': {
            'phone': '+79957744352',
            'name': 'evangelion'
        }
    }
    response = requests.post(url=Config.API_LINK, json=data, headers=Config.API_HEADERS)
    print(response)
    return response.json()