import os
os.environ["DISABLE_SQLALCHEMY_CEXT"] = "1"

from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from models.marca import db, Marca
from models.producto import Producto
from models.usuario import Usuario

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'clave_secreta_discovery_secure' # Necesaria para manejar sesiones de usuario

db.init_app(app)

@app.route('/')
def index():
    try:
        # Obtener parámetros de búsqueda y filtro de la URL
        search_query = request.args.get('q', '').strip()
        marca_filter = request.args.get('marca', '').strip()

        # Consulta base
        query = Producto.query

        # Filtrar por texto si el usuario buscó algo
        if search_query:
            query = query.filter(Producto.nombre.ilike(f'%{search_query}%'))

        # Filtrar por Marca/Categoría si se seleccionó una
        if marca_filter and marca_filter.isdigit():
            query = query.filter(Producto.marca_id == int(marca_filter))

        productos = query.all()
        marcas = Marca.query.all()
    except Exception as e:
        print("\n================ ERROR AL CONSULTAR BD ================")
        print(e)
        print("========================================================\n")
        productos = []
        marcas = []
        
    return render_template('index.html', productos=productos, marcas=marcas)

# Ruta de Registro de Usuarios
@app.route('/registro', methods=['POST'])
def registro():
    try:
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        password = request.form.get('password')

        # Verificar si el correo ya existe
        existe = Usuario.query.filter_by(correo=correo).first()
        if existe:
            return "El correo electrónico ya está registrado.", 400

        nuevo_usuario = Usuario(
            nombre_completo=nombre,
            correo=correo,
            password=password, # En un entorno de producción se recomienda cifrar con bcrypt
            activo=True
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Iniciar sesión automáticamente tras registrarse
        session['usuario_nombre'] = nuevo_usuario.nombre_completo
        session['usuario_correo'] = nuevo_usuario.correo
    except Exception as e:
        print(f"Error en registro: {e}")
    
    return redirect(url_for('index'))

# Ruta de Inicio de Sesión
@app.route('/login', methods=['POST'])
def login():
    try:
        correo = request.form.get('correo')
        password = request.form.get('password')

        usuario = Usuario.query.filter_by(correo=correo, password=password, activo=True).first()
        if usuario:
            session['usuario_nombre'] = usuario.nombre_completo
            session['usuario_correo'] = usuario.correo
        else:
            return "Credenciales inválidas o cuenta inactiva.", 401
    except Exception as e:
        print(f"Error en login: {e}")

    return redirect(url_for('index'))

# Ruta de Cerrar Sesión
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)

# ... resto de rutas ...

# Ruta para agregar un nuevo libro a la base de datos
@app.route('/agregar-producto', methods=['POST'])
def agregar_producto():
    try:
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')
        marca_id = request.form.get('marca_id')
        imagen_url = request.form.get('imagen_url') # Opcional: URL de portada del libro

        nuevo_producto = Producto(
            nombre=nombre,
            precio=precio,
            stock=stock,
            marca_id=marca_id,
            imagen_url=imagen_url
        )
        
        db.session.add(nuevo_producto)
        db.session.commit()
        print("¡Libro agregado exitosamente!")
    except Exception as e:
        db.session.rollback()
        print(f"Error al agregar producto: {e}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)