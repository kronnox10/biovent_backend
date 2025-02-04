import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.os_model import *
from fastapi.encoders import jsonable_encoder
from typing import List


class os_controller:
    
    def create_os(self, os:OS):
        try:
            conn = get_db_connection() 
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM orden_servicio WHERE id_propietario=%s AND id_maquina=%s", (os.id_propietario,os.id_maquina,))
            result = cursor.fetchall()

            if result:
                content = {}    
                content={"Informacion":"Ya hay una os generada para este equipo"}
              
                return jsonable_encoder(content)
            else:   
                cursor.execute("""INSERT INTO orden_servicio (id_propietario, id_maquina, descripcion, id_tecnico, estado) 
                               VALUES (%s,%s,%s,%s,%s)
                               """, (os.id_propietario, os.id_maquina, os.descripcion, os.tecnico, os.estado,))
                conn.commit()
                conn.close()
                return {"resultado": "Orden de servicio registrada"}

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    
    def get_osi(self, os_id: Find_Os):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT orden_servicio.id, propietario.cliente AS propietario_cliente, maquinas.equipo AS nombre_maquina,
                            orden_servicio.descripcion, tecnico.persona_acargo AS tecnico_nombre, orden_servicio.estado
                        FROM orden_servicio
                    INNER JOIN usuario AS propietario ON orden_servicio.id_propietario = propietario.id
                    INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id
                    LEFT JOIN usuario AS tecnico ON orden_servicio.id_tecnico = tecnico.id
                        WHERE propietario.id = %s AND orden_servicio.estado = 1;""", (os_id.id_usuario,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "usuario_cliente":rv[1],
                        "nombre_maquina":rv[2],
                        "descripcion":rv[3],
                        "tecnico":rv[4],
                        "estado":rv[5],
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


    def get_ost(self, os_id: Find_Os):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT orden_servicio.id, propietario.cliente AS propietario_cliente, maquinas.equipo AS nombre_maquina,
                            orden_servicio.descripcion, tecnico.persona_acargo AS tecnico_nombre, orden_servicio.estado
                        FROM orden_servicio
                    INNER JOIN usuario AS propietario ON orden_servicio.id_propietario = propietario.id
                    INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id
                    LEFT JOIN usuario AS tecnico ON orden_servicio.id_tecnico = tecnico.id
                        WHERE orden_servicio.id_tecnico = %s AND orden_servicio.estado = 1;""", (os_id.id_usuario,))
            result = cursor.fetchall()# si, subelo a renderrrrrrrrrrrrrrrrrrrr zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
            payload = []
            content = {} 
            if result:
                
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "usuario_cliente":rv[1],
                        "nombre_maquina":rv[2],
                        "descripcion":rv[3],
                        "tecnico":rv[4],
                        "estado":rv[5],
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
            cursor.execute("""SELECT usuario.cliente, maquinas.equipo, descripcion, tecnico.persona_acargo, orden_servicio.estado 
                           FROM orden_servicio 
                           INNER JOIN usuario ON orden_servicio.id_propietario = usuario.id 
                           INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id 
                           LEFT JOIN usuario AS tecnico ON orden_servicio.id_tecnico = tecnico.id
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
                        "tecnico":rv[3],
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


    def get_os_activas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT orden_servicio.id, propietario.cliente AS propietario_cliente, maquinas.equipo AS nombre_maquina,
                            orden_servicio.descripcion, tecnico.persona_acargo AS tecnico_nombre, orden_servicio.estado
                        FROM orden_servicio
                    INNER JOIN usuario AS propietario ON orden_servicio.id_propietario = propietario.id
                    INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id
                    LEFT JOIN usuario AS tecnico ON orden_servicio.id_tecnico = tecnico.id
                        WHERE orden_servicio.estado = 1;""")
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "usuario_cliente":rv[1],
                        "nombre_maquina":rv[2],
                        "descripcion":rv[3],
                        "tecnico":rv[4],
                        "estado":rv[5],
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

    
    def get_historial_os(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT orden_servicio.id, propietario.cliente AS propietario_cliente, maquinas.equipo AS nombre_maquina,
                            orden_servicio.descripcion, tecnico.persona_acargo AS tecnico_nombre, orden_servicio.estado
                        FROM orden_servicio
                    INNER JOIN usuario AS propietario ON orden_servicio.id_propietario = propietario.id
                    INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id
                    LEFT JOIN usuario AS tecnico ON orden_servicio.id_tecnico = tecnico.id""")
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "usuario_cliente":rv[1],
                        "nombre_maquina":rv[2],
                        "descripcion":rv[3],
                        "tecnico":rv[4],
                        "estado":rv[5],
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


    def asignar_tecnico_os(self, os:OST):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE orden_servicio 
                INNER JOIN usuario
                SET id_tecnico = %s 
                WHERE orden_servicio.id = %s AND usuario.id_rol=3""",(os.id_tecnico, os.id))
            conn.commit()
  
            return {"resultado": "Tecnico asignado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    
        