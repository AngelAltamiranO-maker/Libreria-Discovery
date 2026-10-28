import urllib

class Config:
    # Nombre del servidor y base de datos de SQL Server
    DB_SERVER = r'localhost\sqlexpress'
    DATABASE_NAME = 'Inventarios'
    DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
    
    # Construcción de la URI de conexión para SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://@{DB_SERVER}/{DATABASE_NAME}?driver={DRIVER_NAME}&trusted_connection=yes"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave_secreta_discovery'