import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.usuario_model import *
from fastapi.encoders import jsonable_encoder

class UserController:
    def create_client(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE correo= %s || usuario_l=%s || nic=%s", (user.correo, user.usuario_l, user.nic,))
            result = cursor.fetchall()

            if result:
                content = {}    
                content={"Informacion":"Usuario existente"}
              
                return jsonable_encoder(content)
            else:   
                cursor.execute("""INSERT INTO usuario (id_rol, cliente, correo, usuario_l,contraseña, persona_acargo, telefono, ciudad, direccion, nic, estado,) 
                               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                               """, (user.id_rol, user.cliente, user.correo, user.usuario_l,user.password, user.jefe_de_uso, user.telefono, user.ciudad, user.direccion, user.nic, user.estado,))
                conn.commit()
                conn.close()
                return {"resultado": "Usuario registrado"}

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def login(self, user: Login):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE (correo = %s || usuario_l=%s)  AND contraseña = %s",(user.correo, user.correo, user.password,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'cliente':data[2],
                    'correo':data[3],
                    'usuario':data[4],
                    'contraseña':data[5],
                    'id':data[0],
                    'id_rol':data[1],
                    'persona_acargo':data[6],


                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_clients(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario where id_rol=2")
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "cliente":rv[2],
                        "correo":rv[3],
                        "usuario":rv[4],
                        "contraseña":rv[5],
                        "persona_acargo":rv[6],
                        "telefono":rv[7],
                        "ciudad":rv[8],
                        "direccion":rv[9],
                        "nic":rv[10],
                        "estado":rv[11]
                    }
                    payload.append(content)
            content = {}#
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_tecnicos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id,persona_acargo,estado FROM usuario where id_rol=3")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'Nombre':data[1],
                    'estado':data[2]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def post_client(self, user: User_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id=%s",(user.id,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "cliente":rv[2],
                        "correo":rv[3],
                        "usuario":rv[4],
                        "contraseña":rv[5],
                        "persona_acargo":rv[6],
                        "telefono":rv[7],
                        "ciudad":rv[8],
                        "direccion":rv[9],
                        "nic":rv[10],
                        "estado":rv[11]
                    }
            payload.append(content)
            content = {}#
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()        


    def update_client(self, user: Actualizar):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE usuario
                set 
                cliente=%s,
                correo=%s,
                usuario_l=%s,
                contraseña=%s,
                persona_acargo=%s,
                telefono=%s,
                ciudad=%s,
                direccion=%s,
                nic=%s,
                estado=%s
                WHERE id=%s
                """,(user.cliente, user.correo, user.usuario_l,user.password, user.jefe_de_uso, user.telefono, user.ciudad, user.direccion, user.nic, user.estado, user.id,))
            conn.commit()
  
            return {"resultado": "Usuario actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    


    def get_technicals(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario where id_rol=3")
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "cliente":rv[2],
                        "correo":rv[3],
                        "usuario":rv[4],
                        "contraseña":rv[5],
                        "persona_acargo":rv[6],
                        "telefono":rv[7],
                        "ciudad":rv[8],
                        "direccion":rv[9],
                        "nic":rv[10],
                        "estado":rv[11]
                    }
                    payload.append(content)
            content = {}#
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_technical(self, tecnico: User_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario where id=%s",(tecnico.id,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            if result:
                content={}
                payload=[]
                for rv in result:
                    content={
                        "id":rv[0],
                        "cliente":rv[2],
                        "correo":rv[3],
                        "usuario":rv[4],
                        "contraseña":rv[5],
                        "persona_acargo":rv[6],
                        "telefono":rv[7],
                        "ciudad":rv[8],
                        "direccion":rv[9],
                        "nic":rv[10],
                        "estado":rv[11]
                    }
                    payload.append(content)
            content = {}#
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def create_technical(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE (correo= %s || usuario_l=%s)  || persona_acargo=%s", (user.correo,  user.usuario_l, user.jefe_de_uso,))
            result = cursor.fetchall()

            if result:
                content = {}    
                content={"Informacion":"Usuario existente"}
            
                return jsonable_encoder(content)
            else:   
                cursor.execute("""INSERT INTO usuario (id_rol, cliente, correo, usuario_l, contraseña, persona_acargo, telefono, ciudad, direccion, nic, estado) 
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """, (user.id_rol, user.cliente, user.usuario_l,user.correo, user.password, user.jefe_de_uso, user.telefono, user.ciudad, user.direccion, user.nic, user.estado,))
                conn.commit()
                conn.close()
                return {"resultado": "Usuario registrado"}

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()