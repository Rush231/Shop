from database import db

class Direccion(db.Model):
    __tablename__ = 'direcciones'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    calle = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(50), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    provincia = db.Column(db.String(100), nullable=False)
    codigo_postal = db.Column(db.String(20), nullable=False)

    usuario = db.relationship('Usuario', backref='direcciones')

    def __repr__(self):
        return f'<Direccion {self.id} - Usuario {self.usuario_id}>'
    
    