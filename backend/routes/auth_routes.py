from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from model.Usuario import Usuario

# 1. Creamos el Blueprint (le ponemos de nombre 'auth')
auth_bp = Blueprint('auth', __name__)

# Fíjate que ahora usamos @auth_bp.route en lugar de @app.route
@auth_bp.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    
    # Validamos que vengan todos los datos
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"mensaje": "Faltan datos obligatorios"}), 400
        
    # Verificamos si el usuario ya existe
    usuario_existente = Usuario.query.filter_by(email=data['email']).first()
    if usuario_existente:
        return jsonify({"mensaje": "El email ya está registrado"}), 409
        
    # Encriptamos la contraseña con werkzeug
    password_encriptada = generate_password_hash(data['password'])
    
    # Creamos el usuario
    nuevo_usuario = Usuario(
        username=data['username'],
        email=data['email'],
        password_hash=password_encriptada
    )
    
    # Guardamos en la base de datos
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({"mensaje": "Usuario creado con éxito"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"mensaje": "Error en la base de datos", "error": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"mensaje": "Faltan credenciales"}), 400
        
    # Buscamos al usuario por su email
    usuario = Usuario.query.filter_by(email=data['email']).first()
    
    # Comparamos la contraseña encriptada
    if usuario and check_password_hash(usuario.password_hash, data['password']):
        # Si todo está bien, generamos el Token JWT
        token = create_access_token(identity=str(usuario.id)) 
        return jsonify({
            "mensaje": "Login exitoso",
            "token": token,
            "usuario": {"id": usuario.id, "username": usuario.username, "email": usuario.email}
        }), 200
    else:
        return jsonify({"mensaje": "Email o contraseña incorrectos"}), 401