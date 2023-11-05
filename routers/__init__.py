from flask import Blueprint

# Importa las rutas definidas en main_routes.py
from .main_routes import main_bp

# Registra las rutas en la aplicación
def init_app(app):
    # Registrar el Blueprint en la aplicación
    app.register_blueprint(main_bp, url_prefix='/api')

