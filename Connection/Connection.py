import mysql.connector
from decouple import config

def connect():
    try:
        return mysql.connector.connect(
            host=config('DB_HOST'),
            port=config('DB_PORT'),
            user=config('DB_USERNAME'),
            password=config('DB_PASSWORD'),
            database=config('DB_DATABASE')
        )
    except mysql.connector.Error as error:
        return [{'message':error}]

def connection_insert(cursorObject,insert_stmt, data):
    cursorObject.execute(insert_stmt, data)
    return cursorObject.rowcount

def connection_select(cursorObject,select_stmt):
    cursorObject.execute(select_stmt)
    return cursorObject.fetchall()

def connection_update(cursorObject,update_stmt):
    cursorObject.execute(update_stmt)
    return cursorObject.rowcount