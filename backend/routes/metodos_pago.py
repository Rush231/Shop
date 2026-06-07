from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from model.metodos_pago import MetodoPago

pagos_bp = Blueprint('pagos', __name__)

# Listar métodos de pago del usuario
@pagos_bp.route('/pagos', methods=['GET'])
@jwt_required()
def obtener_pagos():
    usuario_id = get_jwt_identity()
    metodos = MetodoPago.query.filter_by(usuario_id=usuario_id).all()
    
    resultado = [
        {
            "id": m.id,
            "tipo": m.tipo,
            "ultimos_cuatro": m.ultimos_cuatro,
            "marca": m.marca
        } for m in metodos
    ]
    return jsonify(resultado), 200

# Agregar un nuevo método de pago (recibiendo el token de la pasarela)
@pagos_bp.route('/pagos', methods=['POST'])
@jwt_required()
def agregar_pago():
    usuario_id = get_jwt_identity()
    data = request.get_json()
    
    nuevo_pago = MetodoPago(
        usuario_id=usuario_id,
        tipo=data.get('tipo'), # Ej: 'credit_card'
        token_externo=data.get('token'), # Token entregado por MercadoPago/Stripe
        ultimos_cuatro=data.get('ultimos_cuatro'),
        marca=data.get('marca')
    )
    
    db.session.add(nuevo_pago)
    db.session.commit()
    return jsonify({"mensaje": "Método de pago guardado con éxito"}), 201

# Eliminar un método de pago
@pagos_bp.route('/pagos/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_pago(id):
    usuario_id = get_jwt_identity()
    pago = MetodoPago.query.filter_by(id=id, usuario_id=usuario_id).first()
    
    if not pago:
        return jsonify({"error": "Método de pago no encontrado"}), 404
        
    db.session.delete(pago)
    db.session.commit()
    return jsonify({"mensaje": "Método de pago eliminado"}), 200