from database import db

class historial_pedidos(db.Model):
    __tablename__ = 'historial_pedidos'

    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey('ordenes.id'), nullable=False)
    fecha_pedido = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # Ej: pendiente, procesando, enviado, entregado

    orden = db.relationship('Orden', backref=db.backref('historial_pedidos', lazy=True))

    def __repr__(self):
        return f'<HistorialPedido {self.id} - Orden {self.orden_id} - Estado: {self.estado}>'
    
    