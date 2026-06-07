from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from model.pedidos import Pedido
from model.detalle_pedidos import DetallePedido

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/pedidos', methods=['POST'])
@jwt_required()
def crear_pedido():
    usuario_id = get_jwt_identity()
    data = request.get_json()
    
    # 1. Crear el pedido principal
    nuevo_pedido = Pedido(
        usuario_id=usuario_id,
        direccion_id=data['direccion_id'],
        estado='pendiente'
    )
    db.session.add(nuevo_pedido)
    db.session.flush() # Para obtener el ID del pedido sin hacer commit aún
    
    # 2. Crear los detalles (productos del pedido)
    for item in data['productos']:
        detalle = DetallePedido(
            pedido_id=nuevo_pedido.id,
            producto_id=item['producto_id'],
            cantidad=item['cantidad'],
            precio_unitario=item['precio']
        )
        db.session.add(detalle)
        
    db.session.commit()
    return jsonify({"mensaje": "Pedido creado", "pedido_id": nuevo_pedido.id}), 201