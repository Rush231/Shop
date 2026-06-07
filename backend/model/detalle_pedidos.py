from database import db

class Detalle_Pedido(db.Model):
    __tablename__ = 'detalle_pedidos'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False) 
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)

    pedido = db.relationship('Pedido', backref=db.backref('detalle_pedidos', lazy=True))
    producto = db.relationship('Producto')

    def __repr__(self):
        return f'<DetallePedido {self.id} - Pedido {self.Pedido} - Producto {self.producto_id}>'