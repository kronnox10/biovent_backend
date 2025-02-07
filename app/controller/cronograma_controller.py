import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.cronograma_model import *
from fastapi.encoders import jsonable_encoder
from typing import List
import pandas as pd
import numpy as np

class Cronogramacontroller:
    def create_day(self, crono: calendar):   
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("""INSERT INTO cronograma (id_usuario, equipo, enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                """,  (crono.id_usuario, crono.equipo, crono.enero, crono.febrero, crono.marzo, crono.abril, crono.mayo, crono.junio, crono.julio, crono.agosto, crono.septiembre, crono.octubre, crono.noviembre, crono.diciembre))
                conn.commit()
                conn.close()
                return {"resultado": "Cronograma añadido"}

            except mysql.connector.Error as err:
                conn.rollback()
            finally:
                conn.close()

    def getdaysbyuser(self, crono_user: cronouser):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cronograma WHERE id_usuario=%s",(crono_user.id_usuario,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                for rv in result:
                    content = {
                        "id_usuario":rv[0],
                        "equipo":rv[1],
                        "enero":rv[2],
                        "febrero":rv[3],
                        "marzo":rv[4],
                        "abril":rv[5],
                        "mayo":rv[6],
                        "junio":rv[7],
                        "julio":rv[8],
                        "agosto":rv[9],
                        "septiembre":rv[10],
                        "octubre":rv[11],
                        "noviembre":rv[12],
                        "diciembre":rv[13]
                    }
                    payload.append(content)
                json_data = jsonable_encoder(payload)        
            if payload:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Cronograma not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def cargue_masivo_crono(self, file: UploadFile, id_usuario: int):
        conn = None
        try:
        
            df = pd.read_excel(file.file, engine='openpyxl')
            # Validar columnas necesarias
            required_columns = ['EQUIPO', 'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO'
                                , 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
            for col in required_columns:
                if col not in df.columns:
                    return {"error": f"Falta la columna: {col}"}

            
            # Convertir los valores de los meses en "1" o "0", sin afectar la columna "EQUIPO"
            df[required_columns[1:]] = df[required_columns[1:]].applymap(lambda x: "1" if pd.notna(x) and x not in ["", None] else "0")

            # Conectar a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                # Manejar valores nulos o vacíos para evitar errores
                equipo = row['EQUIPO'] if row['EQUIPO'] else "Sin especificar"
                enero = row['ENERO'] 
                febrero = row['FEBRERO']
                marzo = row['MARZO']
                abril = row['ABRIL']
                mayo = row['MAYO'] 
                junio = row['JUNIO'] 
                julio = row['JULIO'] 
                agosto = row['AGOSTO'] 
                septiembre = row['SEPTIEMBRE']
                octubre = row['OCTUBRE'] 
                noviembre = row['NOVIEMBRE']
                diciembre = row['DICIEMBRE'] 

                cursor.execute(
                    """ INSERT INTO cronograma (id_usuario, equipo, enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        id_usuario,
                        equipo,
                        enero,
                        febrero,
                        marzo,
                        abril,
                        mayo,
                        junio,
                        julio,
                        agosto,
                        septiembre,
                        octubre,
                        noviembre,
                        diciembre
                    )
                )
            conn.commit()  # Hacer commit después de todas las inserciones
            return {"resultado": "Cronograma registrado exitosamente"}
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
