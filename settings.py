import os
from dotenv import load_dotenv
load_dotenv()
from datetime import timedelta


# Secret key setting from .env for Flask sessions
SECRET_KEY = os.environ.get('SECRET_KEY')
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)  # after 5 minutes, the user will logout

# DB base configuration from .env for modularity and security reasons
DB = {
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME')
}
