from database import db

class CategoriaProducto(db.Model):
    __tablename__ = 'categoria_productos'

    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)

    def __repr__(self):
        return f'<CategoriaProducto Categoria ID: {self.categoria_id}, Producto ID: {self.producto_id}>'

