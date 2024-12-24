import mysql.connector

"""

def get_db_connection():
    return mysql.connector.connect(
        host="bfrrsop1jsm0voqgbgao-mysql.services.clever-cloud.com",
        user="uupmlcry92arfxpf",
        password="4SPvFuFqzZtr7KeWgCxv",
        database="bfrrsop1jsm0voqgbgao"
    )
"""
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biovent"
    )
    ##importara a xampp