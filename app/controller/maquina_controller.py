import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.maquina_model import Machine
from fastapi.encoders import jsonable_encoder
from typing import List
import pandas as pd


class Machinecontroller:
    def create_machine(self, machine: Machine):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM maquinas WHERE nombre= %s || serial=%s", (machine.nombre,machine.serial,))
            result = cursor.fetchall()

            if result:
                return {"resultado": "Maquina existente"}
            else: 
                cursor.execute("INSERT INTO maquinas (nombre,serial,modelo,marca,inventario,ubicacion) VALUES(%s,%s,%s,%s,%s,%s)",  (machine.nombre,machine.serial,machine.modelo,machine.marca,machine.inventario,machine.ubicacion,))
                conn.commit()
                conn.close()
                return {"resultado": "Maquina registrada"}

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def cargue_masivo(self, file:UploadFile):
        conn=None
        try:#
            # Leer el archivo Excel
            df = pd.read_excel(file.file, engine='openpyxl')
            required_columns = ['nombre','serial','modelo','marca','inventario','ubicacion']
            for col in required_columns:
                if col not in df.columns:
                    return {"error": f"Falta la columna: {col}"}
            
            df = df.where(pd.notnull(df), None)

            # Conectar a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                cursor.execute(
                    "INSERT INTO maquinas (nombre,serial,modelo,marca,inventario,ubicacion) VALUES (%s,%s,%s,%s,%s,%s)",
                    (row['nombre'], row['serial'], row['modelo'], row['marca'], row['inventario'], row['ubicacion'])
                )
            conn.commit()  # Hacer commit después de todas las inserciones
            return {"resultado": "Maquinas añadidas exitosamente"}
        except mysql.connector.Error as err:
            if conn:
                conn.rollback()  # Asegúrate de que conn esté definido
            return {"resultado": str(err)}
        except Exception as e:
            if conn:
                conn.rollback()
            return {"resultado": f"Un error inesperado ocurrió: {str(e)}"}
        finally:
            if conn:
                conn.close()



"""

 def create_user_masivo(self, file: UploadFile):
        conn = None
        try:
            # Leer el archivo Excel
            df = pd.read_excel(file.file, engine='openpyxl')

            required_columns = ['usuario', 'password', 'nombre', 'apellido', 'documento', 'telefono', 'id_rol', 'estado']
            for col in required_columns:
                if col not in df.columns:
                    return {"error": f"Falta la columna: {col}"}
            
            # Conectar a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                cursor.execute(
                    "INSERT INTO usuario (usuario,password,nombre,apellido,documento,telefono,id_rol,estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                    (row['usuario'], row['password'], row['nombre'], row['apellido'], row['documento'], row['telefono'], row['id_rol'], row['estado'])
                )
            
            conn.commit()  # Hacer commit después de todas las inserciones
            return {"resultado": "Users creados exitosamente"}
        except mysql.connector.Error as err:
            if conn:
                conn.rollback()  # Asegúrate de que conn esté definido
            return {"error": str(err)}
        except Exception as e:
            if conn:
                conn.rollback()
            return {"error": f"Un error inesperado ocurrió: {str(e)}"}
        finally:
            if conn:
                conn.close()


"""