from database import db


class MetodoPago(db.Model):
    __tablename__ = 'metodos_pago'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Ej: tarjeta_credito, paypal, etc.
    token_externo = db.Column(db.String(255), nullable=False) # Token de la pasarela
    ultimos_cuatro = db.Column(db.String(4), nullable=True)   # Para mostrar al usuario
    marca = db.Column(db.String(20), nullable=True) #visa, mastercard, etc

    usuario = db.relationship('Usuario', backref='metodos_pago')

    def __repr__(self):
        return f'<MetodoPago {self.id} - Usuario {self.usuario_id} - Tipo: {self.tipo}>'
    
