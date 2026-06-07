import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from model.Usuario import Usuario
from model.categorias import Categoria
from model.productos import Producto  # Asegúrate de usar el nombre con el que guardaste el archivo
from model.imagen_productos import ImagenProducto
from database import db
from model.Usuario import Usuario
from model.productos import productos_bp
# Importamos el Blueprint que acabamos de crear
from routes.auth_routes import auth_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-clave-secreta-temporal')

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# --- REGISTRO DE RUTAS (BLUEPRINTS) ---
# Le decimos a Flask que integre las rutas de auth y les ponga '/api' por delante
app.register_blueprint(auth_bp, url_prefix='/api')

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "success", "message": "Servidor corriendo"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)


    app.register_blueprint(productos_bp, url_prefix='/api')