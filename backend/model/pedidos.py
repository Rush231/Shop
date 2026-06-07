from database import db


class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    direccion_id = db.Column(db.Integer, db.ForeignKey('direcciones.id'), nullable=False)
    fecha_pedido = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(50), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('pedidos', lazy=True))
    direccion = db.relationship('Direccion')

    def __repr__(self):
        return f'<Pedido {self.id} - Usuario {self.usuario_id} - Estado: {self.estado}>'
    
