import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.os_model import *
from fastapi.encoders import jsonable_encoder
from typing import List


class os_controller:
    def get_osi(self, os_id: Find_Os):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT usuario.cliente, maquinas.nombre, descripcion, id_tecnico, orden_servicio.estado 
                           FROM orden_servicio 
                           INNER JOIN usuario ON orden_servicio.id_propietario = usuario.id 
                           INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id 
                           WHERE usuario.id=%s AND orden_servicio.estado = 1;""", (os_id.id_usuario,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                
                content={}
                payload=[]
                for rv in result:
                    content={
                        "usuario_cliente":rv[0],
                        "nombre_maquina":rv[1],
                        "descripcion":rv[2],
                        "id_tecnico":rv[3],
                        "estado":rv[4],
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

    def get_os(self, os_id: Find_Os):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT usuario.cliente, maquinas.nombre, descripcion, id_tecnico, orden_servicio.estado 
                           FROM orden_servicio 
                           INNER JOIN usuario ON orden_servicio.id_propietario = usuario.id 
                           INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id 
                           WHERE usuario.id=%s""", (os_id.id_usuario,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                
                content={}
                payload=[]
                for rv in result:
                    content={
                        "usuario_cliente":rv[0],
                        "nombre_maquina":rv[1],
                        "descripcion":rv[2],
                        "id_tecnico":rv[3],
                        "estado":rv[4],
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