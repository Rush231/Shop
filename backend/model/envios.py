from database import db

class Envio(db.Model):
    __tablename__ = 'envios'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    direccion_id = db.Column(db.Integer, db.ForeignKey('direcciones.id'), nullable=False)
    estado = db.Column(db.String(50), nullable=False, default='pendiente')  # Ej: pendiente, enviado, entregado
    fecha_envio = db.Column(db.DateTime, nullable=True)
    fecha_entrega = db.Column(db.DateTime, nullable=True)

    pedido = db.relationship('Pedido', backref=db.backref('envio', uselist=False))
    direccion = db.relationship('Direccion')

    def __repr__(self):
        return f'<Envio {self.id} - Pedido {self.pedido_id} - Estado: {self.estado}>'
