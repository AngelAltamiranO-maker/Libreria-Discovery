from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Marca(db.Model):
    __tablename__ = 'Marcas'

    id = db.Column('ID', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(50), nullable=False)