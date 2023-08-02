from Connection.Connection import connect,connection_select,connection_insert
  
def getProfileEmail(email):
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = ("SELECT "
                        "idProfile,"
                        "name,"
                        "lastName,"
                        "number,"
                        "birthday,"
                        "email,"
                        "status "
                    "FROM "
                        "profile "
                    "WHERE "
                        "email = '"+email+"'")
            myresult = connection_select(cursorObject,stmt)
            data = myresult[0]
            cursorObject.close()
            dataBase.close()
            return {
                'idProfile': data[0],
                'name': data[1],
                'lastName': data[2],
                'number': data[3],
                'birthday': data[4],
                'email': data[5],
                'status': data[6],
                'flag' : 1
            }
        except:
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 0 ,'error':'getProfileEmail'}
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]
    
def getProfileUser(idUser):
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = ("SELECT "
                        "b.idProfile,"
                        "b.name,"
                        "b.lastName,"
                        "b.number,"
                        "b.birthday,"
                        "b.email,"
                        "b.status,"
                        "c.idRole,"
                        "c.name 'name_role' "
                    "FROM "
                        "user a,"
                        "profile b,"
                        "role c "
                    "WHERE "
                        "a.idProfile = b.idProfile and "
                        "a.idRole = c.idRole and "
                        "a.idUser = '"+idUser+"'")
            myresult = connection_select(cursorObject,stmt)
            data = myresult[0]
            cursorObject.close()
            dataBase.close()
            return {
                'idProfile': data[0],
                'name': data[1],
                'lastName': data[2],
                'number': data[3],
                'birthday': data[4],
                'email': data[5],
                'status': data[6],
                'idRole': data[7],
                'name_role': data[8],
                'flag' : 1
            }
        except:
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 0 ,'error':'getProfileUser'}
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]
    
def postProfile(name,lastName,number,birthday,email,securityResponse):
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = (
                "INSERT INTO profile (name,lastName,number,birthday,email,securityResponse) VALUES (%s, %s, %s, %s,%s, %s)"
            )
            data = (name,lastName,number,birthday,email,securityResponse)
            connection_insert(cursorObject,stmt,data)
            dataBase.commit()
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 1}
        except:
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 0,'error':'postProfile'}
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]