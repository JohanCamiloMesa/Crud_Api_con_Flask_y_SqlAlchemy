import pymysql
from Config.db_config import user, password, host, database

def init_database():
    try:
        # Primero intentamos conectar a la base de datos existente
        try:
            conn = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset='utf8mb4'
            )
            print(f"Database '{database}' already exists!")
            return  # Si la conexión es exitosa, la base de datos ya existe
        except pymysql.Error as err:
            if err.args[0] == 1049:  # Unknown database error code
                # La base de datos no existe, la crearemos
                conn = pymysql.connect(
                    host=host,
                    user=user,
                    password=password,
                    charset='utf8mb4'
                )
                cursor = conn.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
                print(f"Database '{database}' created successfully!")
            else:
                # Otro tipo de error
                raise

    except pymysql.Error as err:
        print(f"Error: {err}")
        raise

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()