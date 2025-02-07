import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.cronograma_model import *
from fastapi.encoders import jsonable_encoder
from typing import List
import pandas as pd


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


    def cargue_masivo(self, file: UploadFile, id_usuario: int):
        conn = None
        try:
        
            df = pd.read_excel(file.file, engine='openpyxl')
            # Validar columnas necesarias
            required_columns = ['EQUIPO', 'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO'
                                , 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
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
                enero = row['ENERO'] if row['ENERO'] else "0"
                febrero = row['FEBRERO'] if row['FEBRERO'] else "0"
                marzo = row['MARZO'] if row['MARZO'] else "0"
                abril = row['ABRIL'] if row['ABRIL'] else "0"
                mayo = row['MAYO'] if row['MAYO'] else "0"
                junio = row['JUNIO'] if row['JUNIO'] else "0"
                julio = row['JULIO'] if row['JULIO'] else "0"
                agosto = row['AGOSTO'] if row['AGOSTO'] else "0"
                septiembre = row['SEPTIEMBRE'] if row['SEPTIEMBRE'] else "0"
                octubre = row['OCTUBRE'] if row['OCTUBRE'] else "0"
                noviembre = row['NOVIEMBRE'] if  row['NOVIEMBRE'] else "0"
                diciembre = row['DICIEMBRE'] if row['DICIEMBRE'] else "0"

                cursor.execute(
                    """DELETE 
                        INSERT INTO cronograma (id_usuario, equipo, enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre)
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
