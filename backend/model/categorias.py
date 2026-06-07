from database import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

    # Relación inversa: para ver todos los productos de una categoría
    productos = db.relationship('Producto', backref='categoria', lazy=True)

    def __repr__(self):
        return f'<Categoria {self.nombre}>'