import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_key'
    API_LINK = 'https://order.drcash.sh/v1/order'
    API_HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer RLPUUOQAMIKSAB2PSGUECA'
    }
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'app.db')