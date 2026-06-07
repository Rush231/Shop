from database import db

class ImagenProducto(db.Model):
    __tablename__ = 'imagen_productos'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id', ondelete='CASCADE'), nullable=False)
    es_principal = db.Column(db.Boolean, default=False)
    url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Imagen {self.id} (Principal: {self.es_principal})>'