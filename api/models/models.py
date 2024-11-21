import pymysql
import os
import base64

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
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_database};")
            cursor.execute(f"USE {db_database};")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id_product INT AUTO_INCREMENT PRIMARY KEY,
                    imagen_64 TEXT,
                    nombre_producto VARCHAR(255) NOT NULL
                );
            """)
            print("Tabla 'productos' verificada/creada.")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    password VARCHAR(255) NOT NULL,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    role VARCHAR(50) NOT NULL
                );
            """)
            print("Tabla 'usuarios' verificada/creada.")

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

            ruta_imagen = "multimedia/Logo.jpg"  
            with open(ruta_imagen, "rb") as file:
                imagen_bytes = file.read()
            imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')

            query_check = "SELECT COUNT(*) FROM productos WHERE nombre_producto = %s"
            cursor.execute(query_check, ("Logo",))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                query_insert = "INSERT INTO productos (nombre_producto, imagen_64) VALUES (%s, %s)"
                cursor.execute(query_insert, ("Logo", imagen_base64))
                print("Producto 'Logo' insertado correctamente.")
            else:
                print("El producto 'Logo' ya existe en la base de datos.")
            
            connection.commit()
            print("Cambios confirmados en la base de datos.")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
        return None




