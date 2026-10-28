from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Marca(db.Model):
    __tablename__ = 'Marcas'
    __table_args__ = {'schema': 'dbo'}

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(50), nullable=False)

    # Relación de uno a muchos con Productos
    productos = db.relationship('Producto', backref='marca', lazy=True)