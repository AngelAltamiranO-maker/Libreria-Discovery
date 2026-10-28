import uuid
from datetime import datetime
from models.marca import db

class Usuario(db.Model):
    __tablename__ = 'Usuarios'

    id = db.Column('Id', db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre_completo = db.Column('NombreCompleto', db.String(120), nullable=True)
    correo = db.Column('CorreoElectronico', db.String(150), nullable=True, unique=True)
    password = db.Column('Password', db.String(250), nullable=True)
    activo = db.Column('Activo', db.Boolean, default=True)
    fecha_registro = db.Column('FechaRegistro', db.DateTime, default=datetime.utcnow)