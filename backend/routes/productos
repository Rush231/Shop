from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from model.productos import Producto
from model.categorias import Categoria

# Creamos el Blueprint para los productos
productos_bp = Blueprint('productos', __name__)

# --- RUTA PÚBLICA: Ver todos los productos ---
@productos_bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    resultado = []
    for p in productos:
        resultado.append({
            "id": p.id,
            "nombre": p.nombre,
            "precio": float(p.precio), # Convertimos a float para que JSON lo entienda
            "stock": p.stock,
            "condicion": p.condicion,
            "vendedor_id": p.vendedor_id
        })
    return jsonify(resultado), 200

# --- RUTA PRIVADA: Crear un producto ---
# El decorador @jwt_required() es la seguridad: exige que venga un Token válido en la petición
@productos_bp.route('/productos', methods=['POST'])
@jwt_required() 
def crear_producto():
    # get_jwt_identity() saca el 'id' del usuario directamente desde el token validado
    usuario_id = get_jwt_identity() 
    data = request.get_json()

    # Validación básica
    if not data or not data.get('nombre') or not data.get('precio') or not data.get('stock') or not data.get('categoria_id'):
        return jsonify({"mensaje": "Faltan datos obligatorios para crear el producto"}), 400

    # Verificamos que la categoría exista antes de usarla
    categoria = Categoria.query.get(data['categoria_id'])
    if not categoria:
        return jsonify({"mensaje": "La categoría indicada no existe"}), 404

    nuevo_producto = Producto(
        nombre=data['nombre'],
        descripcion=data.get('descripcion', 'Sin descripción'),
        precio=data['precio'],
        stock=data['stock'],
        vendedor_id=usuario_id,  # ¡Asignamos como vendedor al dueño del token automáticamente!
        categoria_id=data['categoria_id'],
        condicion=data.get('condicion', 'nuevo'),
        envio_gratis=data.get('envio_gratis', False),
        es_importado=data.get('es_importado', False)
    )

    try:
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({"mensaje": "Producto publicado con éxito", "producto_id": nuevo_producto.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"mensaje": "Error al guardar el producto", "error": str(e)}), 500