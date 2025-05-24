import os
from datetime import timedelta

class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    MONGO_URI = os.getenv("MONGO_URI")
    
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_DB = 'newsBloom'
    MYSQL_PASSWORD = ''
    MYSQL_CURSORCLASS = "DictCursor"

    BCRYPT_LOG_ROUNDS = 14

    JWT_SECRET_KEY = 'Hello this is jwt secret key'
    JWT_TOKEN_LOCATION = 'cookies'
    JWT_ACCESS_COOKIE_NAME = "access_token"
    
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)