from database import db

class Valoracion(db.Model):
    __tablename__ = 'valoraciones'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    puntuacion = db.Column(db.Integer, nullable=False)  # Puntuación del 1 al 5
    comentario = db.Column(db.Text)

    usuario = db.relationship('Usuario', backref='valoraciones')
    producto = db.relationship('Producto', backref='valoraciones')

    def __repr__(self):
        return f'<Valoracion {self.id} - Usuario {self.usuario_id} - Producto {self.producto_id} - Puntuacion: {self.puntuacion}>'
    
    