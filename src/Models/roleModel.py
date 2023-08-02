from Connection.Connection import connect,connection_select
def getRoleAll():
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = "SELECT idRole,name FROM role"
            myresult = connection_select(cursorObject,stmt)
            cursorObject.close()
            dataBase.close()
            return myresult
        except:
            cursorObject.close()
            dataBase.close()
            return  [{'message':'Error en consulta getRoleAll'}]
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]