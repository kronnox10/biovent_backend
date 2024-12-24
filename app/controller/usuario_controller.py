import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.usuario_model import User, Login
from fastapi.encoders import jsonable_encoder

class UserController:
    def create_user(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE usuario= %s", (user.usuario,))
            result = cursor.fetchall()

            if result:
                content = {}    
                content={"Informacion":"Usuario existente"}
              
                return jsonable_encoder(content)
            else:   
                cursor.execute("INSERT INTO usuario (id_rol,usuario,password,) VALUES (%s,%s,%s)", (user.id_rol,user.usuario,user.password,))
                conn.commit()
                conn.close()
                id=cursor.lastrowid
                return {id}#aja

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()



    def login(self, user: Login):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE Correo = %s AND Contraseña = %s",(user.usuario, user.password,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'correo':data[2],
                    'password':data[3],
                    'nombre':data[4],
                    'id':data[0],
                    'id_rol':data[1],


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