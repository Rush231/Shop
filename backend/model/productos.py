from database import db
class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    condicion = db.Column(db.String(50), default='nuevo', nullable=False)
    estado_publicacion = db.Column(db.String(50), default='activa', nullable=False)
    imagenes = db.relationship('ImagenProducto', backref='producto', lazy=True, cascade="all, delete-orphan")
    envio_gratis = db.Column(db.Boolean, default=False)
    es_importado = db.Column(db.Boolean, default=False)

    # atributos = db.relationship('AtributoProducto', backref='producto', lazy=True, cascade="all, delete-orphan")
    def __repr__(self):
        return f'<Producto {self.nombre} - Stock: {self.stock}>'
    
