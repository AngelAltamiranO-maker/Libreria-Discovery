import uuid
from models.marca import db

class Producto(db.Model):
    __tablename__ = 'Productos'

    id = db.Column('ID', db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column('Descripcion', db.String(100), nullable=False)
    precio = db.Column('Precio', db.Numeric(10, 2), nullable=False)
    stock = db.Column('Existencia', db.Integer, nullable=False)
    # Apuntamos directamente al nombre de la tabla y columna en la BD para evitar conflictos de carga cruzada
    marca_id = db.Column('IdMarca', db.Integer, db.ForeignKey('Marcas.ID'), nullable=False)

    # Relación por nombre de clase en cadena ('Marca')
    marca = db.relationship('Marca', backref=db.backref('productos', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': float(self.precio),
            'stock': self.stock,
            'marca_id': self.marca_id
        }