import pymysql
import os

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_NAME')

def conexion():
    try:
        connection = pymysql.connect(
            host=db_host,  
            user=db_user,
            password=db_password, 
            database=db_database,
        )
        with connection.cursor() as cursor:
            # Crear la base de datos si no existe
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_database};")
            # Seleccionar la base de datos
            cursor.execute(f"USE {db_database};")

            # Crear la tabla productos si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id_product INT AUTO_INCREMENT PRIMARY KEY,
                    imagen_64 TEXT,
                    nombre_producto VARCHAR(255) NOT NULL
                );
            """)
            print("Tabla 'productos' verificada/creada.")

            # Crear la tabla usuarios si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    password VARCHAR(255) NOT NULL,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    role VARCHAR(50) NOT NULL
                );
            """)
            print("Tabla 'usuarios' verificada/creada.")

            # Crear la tabla ordenes si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ordenes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    pedido_id VARCHAR(255),
                    imagen LONGTEXT,
                    nombre_producto VARCHAR(255) NOT NULL,
                    cantidad INT NOT NULL
                );
            """)
            print("Tabla ordenes lista")

            # Confirmar cambios
            connection.commit()
            print("Cambios confirmados en la base de datos.")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
        return None




