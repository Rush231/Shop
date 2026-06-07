from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from model.ofertas import Oferta
from model.productos import Producto

ofertas_bp = Blueprint('ofertas', __name__)

@ofertas_bp.route('/ofertas', methods=['POST'])
@jwt_required() 
def crear_oferta():
    data = request.get_json()
    
    # Validar que el producto exista
    producto = Producto.query.get(data['producto_id'])
    if not producto:
        return jsonify({"mensaje": "Producto no encontrado"}), 404
    
    nueva_oferta = Oferta(
        producto_id=data['producto_id'],
        descuento=data['descuento'],
        fecha_inicio=data['fecha_inicio'],
        fecha_fin=data['fecha_fin']
    )
    
    db.session.add(nueva_oferta)
    db.session.commit()
    
    return jsonify({"mensaje": "Oferta creada", "oferta_id": nueva_oferta.id}), 201