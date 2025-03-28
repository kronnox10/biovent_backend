import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.maquina_model import *
from fastapi.encoders import jsonable_encoder
from typing import List
import pandas as pd


class Machinecontroller:
    def create_machine(self, machine: Machine):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM maquinas WHERE equipo= %s", (machine.nombre,))
            result = cursor.fetchall()

            if result:#ok
                return {"resultado": "Maquina existente"}
            else: 
                cursor.execute("""INSERT INTO maquinas (id_usuario, equipo, marca, modelo, serie, activo, ubicacion, sede, estado, desc_estado)
                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                               """,  (machine.id_user, machine.nombre, machine.marca, machine.modelo, machine.serial ,machine.inventario ,machine.ubicacion, machine.sede ,machine.estado, machine.descripcion_e))
                conn.commit()
                conn.close()
                return {"resultado": "Maquina añadida"}

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def cargue_masivo(self, file: UploadFile, id_usuario: int):
        conn = None
        try:
        
            df = pd.read_excel(file.file, engine='openpyxl')
            # Validar columnas necesarias
            required_columns = ['EQUIPO', 'MARCA', 'MODELO', 'SERIE', 'ACTIVO', 'UBICACIÓN', 'SEDE']
            for col in required_columns:
                if col not in df.columns:
                    return {"error": f"Falta la columna: {col}"}

            # Reemplazar NaN con None para compatibilidad con la base de datos
            df = df.where(pd.notnull(df), None)

            # Conectar a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                # Manejar valores nulos o vacíos para evitar errores
                equipo = row['EQUIPO'] if row['EQUIPO'] else "Sin especificar"
                marca = row['MARCA'] if row['MARCA'] else "Sin marca"
                modelo = row['MODELO'] if row['MODELO'] else "Sin modelo"
                serie = row['SERIE'] if row['SERIE'] else "Sin serie"
                activo = row['ACTIVO'] if row['ACTIVO'] else "Sin inventario"
                ubicacion = row['UBICACIÓN'] if row['UBICACIÓN'] else "Desconocida"
                sede = row['SEDE'] if row['SEDE'] else "Sin sede"

                cursor.execute(
                    """
                   INSERT INTO maquinas (id_usuario, equipo, marca, modelo, serie, activo, ubicacion, sede, estado, desc_estado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        id_usuario,
                        equipo,
                        marca,
                        modelo,
                        serie,
                        activo,
                        ubicacion,
                        sede,
                        True,  
                        None  
                    )
                )
            conn.commit()  # Hacer commit después de todas las inserciones
            return {"resultado": "Maquinas añadidas exitosamente"}
        except mysql.connector.Error as err:
            if conn:
                conn.rollback()
            return {"resultado": str(err)}
        except Exception as e:
            if conn:
                conn.rollback()
            return {"resultado": f"Un error inesperado ocurrió: {str(e)}"}
        finally:
            if conn:
                conn.close()


    def get_machines(self, machine_id: Machinima):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM maquinas WHERE id=%s",(machine_id.id,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "id_usuario":rv[1],
                        "nombre":rv[2],
                        "marca":rv[3],
                        "modelo":rv[4],
                        "serial":rv[5],
                        "inventario":rv[6],
                        "ubicacion":rv[7],
                        "sede":rv[8],
                        "estado":rv[9],
                        "desc_estado":rv[10]
                    }
                    payload.append(content)
            content = {}#
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="maquina not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_machine(self, machine_id: Find_machine):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM maquinas WHERE id_usuario=%s", (machine_id.id_usuario,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "id_usuario":rv[1],
                        "nombre":rv[2],
                        "marca":rv[3],
                        "modelo":rv[4],
                        "serial":rv[5],
                        "inventario":rv[6],
                        "ubicacion":rv[7],
                        "sede":rv[8],
                        "estado":rv[9],
                        "desc_estado":rv[10]
                    }
                    payload.append(content)
            content = {}#
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="maquina not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_maquina(self, machine: UpdateMachine):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE maquinas
                set 
                equipo=%s,
                marca=%s,
                modelo=%s,
                serie=%s,
                activo=%s,
                ubicacion=%s,
                sede=%s,
                estado=%s,
                desc_estado=%s
                WHERE id=%s""",(machine.nombre, machine.marca, machine.modelo, machine.serial ,machine.inventario ,machine.ubicacion, machine.sede, machine.estado, machine.descripcion_e, machine.id,))
            conn.commit()
  
            return {"resultado": "Maquina actualizada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    


    def up_est_mac(self, machine: Machinima):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE maquinas
                set estado=0
                WHERE id=%s""",(machine.id,))
            conn.commit()
  
            return {"resultado": "La maquina se apago"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    



    def get_machine_on(self, machine: machineon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(id) as Funcionando
                            FROM maquinas
                            WHERE id_usuario = %s AND estado=1""",(machine.id_usuario,))
            result = cursor.fetchone() 
            if result:
                return {"Funcionando": result[0]}
            else:
                raise HTTPException(status_code=404, detail="Máquinas no encontradas") 
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")
        finally:
            cursor.close()  # Asegúrate de cerrar el cursor
            conn.close()


    def get_machine_off(self, machine: machineon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(id) as Dañados 
                           FROM maquinas 
                           WHERE id_usuario =%s AND estado = 0 AND (desc_estado="" OR desc_estado IS NULL) """,(machine.id_usuario,))
            result = cursor.fetchone() 
            if result:
                return {"Dañadas": result[0]}
            else:
                raise HTTPException(status_code=404, detail="Máquinas no encontradas") 
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")
        finally:
            cursor.close()  # Asegúrate de cerrar el cursor
            conn.close()


    def get_machine_off_topic(self, machine: machineon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(id) as Dañadas_por_algo 
                            FROM maquinas
                            WHERE id_usuario = %s AND estado = 0 AND desc_estado IS NOT NULL AND desc_estado <> '' """,(machine.id_usuario,))
            result = cursor.fetchone() 
            if result:
                return {"Dañadasporalgo": result[0]}
            else:
                raise HTTPException(status_code=404, detail="Máquinas no encontradas") 
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")
        finally:
            cursor.close()  # Asegúrate de cerrar el cursor
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