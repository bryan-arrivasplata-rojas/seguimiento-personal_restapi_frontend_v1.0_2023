from Connection.Connection import connect,connection_insert,connection_select,connection_update

def getUserAll():
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = ("SELECT "
                        "a.code,b.name,b.lastName,b.number,b.birthday,b.email,a.idRole,c.name 'name_role',a.idUser "
                    "FROM "
                        "user a,"
                        "profile b,"
                        "role c "
                    "WHERE "
                        "a.idProfile=b.idProfile and "
                        "a.idRole=c.idRole "
                    "ORDER BY "
                        "a.code ASC")
            myresult = connection_select(cursorObject,stmt)
            cursorObject.close()
            dataBase.close()
            return myresult
        except:
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 0 ,'error':'getUserAll'}
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]

def getUser(code,password):
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = ("SELECT "
                        "a.code,b.name,b.lastName,b.number,b.birthday,b.email,b.securityResponse,a.idRole,c.name 'name_role',a.idUser "
                    "FROM "
                        "user a,"
                        "profile b, "
                        "role c "
                    "WHERE "
                        "a.code = '"+code+"' and "
                        "a.password = '"+password+"' and "
                        "a.idProfile=b.idProfile and "
                        "a.idRole=c.idRole")
            myresult = connection_select(cursorObject,stmt)
            data = myresult[0]
            cursorObject.close()
            dataBase.close()
            return {
                'code': data[0],
                'name':data[1],
                'lastName':data[2],
                'number':data[3],
                'birthday':data[4],
                'email':data[5],
                'securityResponse':data[6],
                'idRole':data[7],
                'name_role':data[8],
                'idUser':data[9],
                'flag' : 1
            }
        except:
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 0 ,'error':'getUser'}
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]

def getUserPasswordSecurity(code,securityResponse):
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = ("SELECT "
                        "a.code,a.password "
                    "FROM "
                        "user a,"
                        "profile b "
                    "WHERE "
                        "a.code = '"+code+"' and "
                        "b.securityResponse = '"+securityResponse+"' and "
                        "a.idProfile=b.idProfile")
            myresult = connection_select(cursorObject,stmt)
            data = myresult[0]
            cursorObject.close()
            dataBase.close()
            return {
                'code': data[0],
                'password':data[1],
                'flag' : 1
            }
        except:
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 0 ,'error':'getUserPasswordSecurity'}
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]

def postUser(code,password,idProfile):
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = (
            "INSERT INTO user (code,password,idProfile) VALUES (%s, %s, %s)"
            )
            data = (code,password,idProfile)
            connection_insert(cursorObject,stmt,data)
            dataBase.commit()
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 1}
        except:
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 0,'error':'postUser' }
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]


def putUser(idUser,idRole):
    dataBase = connect()
    if not (isinstance(dataBase, list)):
        cursorObject = dataBase.cursor()
        try:
            stmt = (
                "UPDATE user set idRole='"+idRole+"' WHERE idUser='"+idUser+"'"
            )
            connection_update(cursorObject,stmt)
            dataBase.commit()
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 1}
        except:
            cursorObject.close()
            dataBase.close()
            return { 'flag' : 0,'error':'putUser' }
    else:
        error_message = dataBase[0]['message']
        return [{'message':error_message}]