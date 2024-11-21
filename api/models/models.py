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

            cursor.execute("INSERT INTO productos(nombre_producto, imagen_64) VALUES(Logo,https://www.canva.com/design/DAGN3kS7gF0/35xQRsI9s-R60_f-s8DuUQ/watch?utm_content=DAGN3kS7gF0&utm_campaign=designshare&utm_medium=link&utm_source=editor)")

            connection.commit()
            print("Cambios confirmados en la base de datos.")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
        return None




