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