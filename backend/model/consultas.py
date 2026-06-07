from database import db


class Consulta(db.Model):
    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True)
    
    # ¿De qué producto es la pregunta?
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id', ondelete='CASCADE'), nullable=False)
    
    # ¿Quién hace la pregunta? (El comprador)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False) 
    
    # La pregunta en sí
    mensaje = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # --- LA RESPUESTA DEL VENDEDOR ---
    # Al principio es 'nullable=True' porque cuando el comprador pregunta, todavía no hay respuesta
    respuesta = db.Column(db.Text, nullable=True) 
    fecha_respuesta = db.Column(db.DateTime, nullable=True)

    # Relaciones (opcionales, para facilitar búsquedas)
    producto = db.relationship('Producto', backref=db.backref('consultas', lazy=True, cascade="all, delete-orphan"))
    usuario = db.relationship('Usuario', backref='mis_preguntas')

    def __repr__(self):
        return f'<Consulta {self.id} - Producto {self.producto_id}>'