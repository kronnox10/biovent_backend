import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.usuario_model import User, Login, User_id 
from fastapi.encoders import jsonable_encoder

class UserController:
    
    def create_client(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE correo= %s  || nic=%s", (user.correo, user.nic,))
            result = cursor.fetchall()

            if result:
                content = {}    
                content={"Informacion":"Usuario existente"}
              
                return jsonable_encoder(content)
            else:   
                cursor.execute("""INSERT INTO usuario (id_rol, cliente, correo, contraseña, persona_acargo, telefono, ciudad, direccion, nic, estado) 
                               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                               """, (user.id_rol,user.cliente, user.correo,user.password,user.jefe_de_uso, user.telefono, user.ciudad, user.direccion, user.nic, user.estado,))
                conn.commit()
                conn.close()
                id=cursor.lastrowid
                return {id}#

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def login(self, user: Login):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE correo = %s AND contraseña = %s",(user.correo, user.password,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'cliente':data[2],
                    'correo':data[3],
                    'contraseña':data[4],
                    'id':data[0],
                    'id_rol':data[1],
                    'persona_acargo':data[5],


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
            cursor.execute("SELECT * FROM usuario")
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
                        "contraseña":rv[4],
                        "persona_acargo":rv[5],
                        "telefono":rv[6],
                        "ciudad":rv[7],
                        "direccion":rv[8],
                        "nic":rv[9],
                        "estado":rv[10]
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
                        "contraseña":rv[4],
                        "persona_acargo":rv[5],
                        "telefono":rv[6],
                        "ciudad":rv[7],
                        "direccion":rv[8],
                        "nic":rv[9],
                        "estado":rv[10]
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


    def update_client(self, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE usuario
                            set 
                            cliente=%s,
                            correo=%s,
                            contraseña=%s,
                            persona_acargo=%s,
                            telefono=%s,
                            ciudad=%s,
                            direccion=%s,
                            nic=%s,
                            estado=%s
                           
                            WHERE id=%s
                           """,(user.cliente, user.correo, user.password, user.jefe_de_uso, user.telefono, user.ciudad, user.direccion, user.nic, user.estado,))
            conn.commit()
  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
