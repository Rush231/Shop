from database import db

class detalle_pedidos(db.Model):
    __tablename__ = 'detalle_pedidos'

    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey('ordenes.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)

    orden = db.relationship('Orden', backref=db.backref('detalle_pedidos', lazy=True))
    producto = db.relationship('Producto')

    def __repr__(self):
        return f'<DetallePedido {self.id} - Orden {self.orden_id} - Producto {self.producto_id}>'