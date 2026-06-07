from database import db


class Oferta(db.Model):
    __tablename__ = 'ofertas'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    descuento = db.Column(db.Float, nullable=False)  # Porcentaje de descuento
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=False)

    producto = db.relationship('Producto', backref=db.backref('ofertas', lazy=True))

    def __repr__(self):
        return f'<Oferta {self.id} - Producto {self.producto_id} - Descuento: {self.descuento}%>'