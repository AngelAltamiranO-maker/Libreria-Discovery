from flask import Blueprint, render_template, jsonify
from models.marca import Marca
from models.producto import Producto

store_bp = Blueprint('store_bp', __name__)

@store_bp.route('/')
def index():
    productos = Producto.query.all()
    marcas = Marca.query.all()
    # Debe decir exactamente 'index.html'
    return render_template('index.html', productos=productos, marcas=marcas)