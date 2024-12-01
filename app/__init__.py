from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', 'clave-secreta')

    # Cargar variables de entorno
    load_dotenv()

    # Registrar blueprints
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.usuario import user_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(user_bp, url_prefix="/user")

    return app