import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

def get_db_connection():
    import psycopg2
    return psycopg2.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )