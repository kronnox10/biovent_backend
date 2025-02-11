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
    

    def update_os(self, os:OSUpdate, pos:pendiente_os ):        
        
        try:
            conn = get_db_connection() 
            cursor = conn.cursor()
            cursor.execute("SELECT id_os FROM maquinas_pendientes WHERE id_os=%s", (os.id,))
            result = cursor.fetchall()

            if result:
                cursor.execute("""UPDATE maquinas_pendientes
                           set descripcion_t=%s, repuestos=%s, estado=%s
                            WHERE id_os=%s
                            """,(pos.descripcion, pos.repuestos, pos.estado_p,os.id,))

                cursor.execute("""UPDATE orden_servicio as os
                INNER JOIN maquinas as machine ON os.id_maquina = machine.id
                set  os.estado=%s, machine.estado=%s
                WHERE os.id=%s""",(os.estado,os.estado_machine,os.id,))
                conn.commit()
            else:   
                cursor.execute("""INSERT INTO maquinas_pendientes (id_os, id_propietario, id_maquina, descripcion_t, repuestos, estado) 
                           VALUES(%s,%s,%s,%s,%s,%s)                       
                        """,(pos.id_os, pos.id_maquina_p, pos.id_propietario, pos.descripcion, pos.repuestos, pos.estado_p,))

                cursor.execute("""UPDATE orden_servicio as os
                INNER JOIN maquinas as machine ON os.id_maquina = machine.id
                set  os.estado=%s, machine.estado=%s
                WHERE os.id=%s""",(os.estado,os.estado_machine,os.id,))
                conn.commit()
            
            return {"resultado": "Os realizado satisfactoriamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
            return {"error": f"Error al actualizar la OS: {err}"}
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
                            orden_servicio.descripcion, tecnico.persona_acargo AS tecnico_nombre, orden_servicio.estado,
                            orden_servicio.id_maquina AS id_maquina, orden_servicio.id_propietario AS id_propietario
                           FROM orden_servicio
                    INNER JOIN usuario AS propietario ON orden_servicio.id_propietario = propietario.id
                    INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id
                    LEFT JOIN usuario AS tecnico ON orden_servicio.id_tecnico = tecnico.id
                        WHERE orden_servicio.id_tecnico = %s AND orden_servicio.estado = 1;""", (os_id.id_usuario,))
            result = cursor.fetchall()# 
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
                        "maquina":rv[6],
                        "dueño":rv[7],
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
        
    
    def get_osh(self, os_id: Find_Os):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT orden_servicio.id, propietario.cliente AS propietario_cliente, maquinas.equipo AS nombre_maquina,
                            orden_servicio.descripcion, tecnico.persona_acargo AS tecnico_nombre, orden_servicio.estado
                        FROM orden_servicio
                    INNER JOIN usuario AS propietario ON orden_servicio.id_propietario = propietario.id
                    INNER JOIN maquinas ON orden_servicio.id_maquina = maquinas.id
                    LEFT JOIN usuario AS tecnico ON orden_servicio.id_tecnico = tecnico.id
                        WHERE orden_servicio.id_tecnico = %s AND orden_servicio.estado = 0;""", (os_id.id_usuario,))
            result = cursor.fetchall()# 
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
        