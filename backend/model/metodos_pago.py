from database import db


class metodos_pago(db.Model):
    __tablename__ = 'metodos_pago'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Ej: tarjeta_credito, paypal, etc.
    detalles = db.Column(db.String(255), nullable=False)  # Ej: número de tarjeta enmascarado

    usuario = db.relationship('Usuario', backref='metodos_pago')

    def __repr__(self):
        return f'<MetodoPago {self.id} - Usuario {self.usuario_id} - Tipo: {self.tipo}>'
    
    