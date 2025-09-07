import mysql.connector
from Config.db_config import user, password, host, database

def init_database():
    try:
        # Primero intentamos conectar a la base de datos existente
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print(f"Database '{database}' already exists!")
            return  # Si la conexión es exitosa, la base de datos ya existe
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                # La base de datos no existe, la crearemos
                conn = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password
                )
                cursor = conn.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
                print(f"Database '{database}' created successfully!")
            else:
                # Otro tipo de error
                raise

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()