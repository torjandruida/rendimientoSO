import cx_Oracle




def getConnection():
    host = "localhost"
    user = "SYSTEM"
    passw = "Orcl12345"
    tsname = "ORCL"

    try:
        connection = cx_Oracle.connect(user, passw, host+"/"+tsname)
    except Exception as error:
        print("no se pudo conectar a la nase de datos " + error)
    else:
        print("conexion realizada")

    return connection

def fetchData():
    connection = getConnection()
    cursor = connection.cursor()
    sql_fetch_date = "select * from servicios"
    cursor.execute(sql_fetch_date)
    listaTupla = []
    for result in cursor:
        listaTupla.append(result)

    connection.commit()
    cursor.close()
    return listaTupla

def insertData():
    connection = getConnection()
    cursor = connection.cursor()
    p1 = "insert into servicios values (3,'camara','camara','fotografica')"
    cursor.execute(p1)
    connection.commit()
    cursor.close()
    print("servicio agregado")

def updateData():
    connection = getConnection()
    cursor = connection.cursor()
    sql_update = "update servicios set descripcion='camara alta resolucion' where id_servicios=3"
    cursor.execute(sql_update)
    connection.commit()
    cursor.close()
    print("servicio actualizado")

def deleteData():
    connection = getConnection()
    cursor = connection.cursor()
    sql_delete = "delete from servicios where id_servicios=3"
    cursor.execute(sql_delete)
    connection.commit()
    cursor.close()
    print("servicio borrado")

if __name__ == "__main__":
    pass
