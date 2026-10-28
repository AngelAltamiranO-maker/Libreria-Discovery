from flask import Blueprint, render_template, jsonify
from models.marca import Marca
from models.producto import Producto

store_bp = Blueprint('store_bp', __name__)

@store_bp.route('/')
def index():
    # Consulta a la Base de Datos mediante ORM (Equivalente a Entity Framework)
    productos = Producto.query.all()
    marcas = Marca.query.all()
    return render_template('index.html', productos=productos, marcas=marcas)

@store_bp.route('/api/productos')
def obtener_productos_json():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos])