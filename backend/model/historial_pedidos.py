from database import db

class Historial_Pedido(db.Model):
    __tablename__ = 'historial_pedidos'

    id = db.Column(db.Integer, primary_key=True)
    Pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    fecha_pedido = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # Ej: pendiente, procesando, enviado, entregado

    pedido = db.relationship('Pedido', backref=db.backref('historial_pedidos', lazy=True))

    def __repr__(self):
        return f'<HistorialPedido {self.id} - Pedido {self.Pedido_id} - Estado: {self.estado}>'
    
