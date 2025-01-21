import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="bmek95iuaecirph74akm-mysql.services.clever-cloud.com",
        user="uh29isq44hisbkut",
        password="I946d1LnDR0pEHspueVx",
        database="bmek95iuaecirph74akm"
    )

"""
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biovent"
    )
    ##importara a xampp"""