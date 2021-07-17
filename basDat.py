import cx_Oracle


class conect():

    def __init__(self):
        host = "localhost"
        user = "SYSTEM"
        passw = "Orcl12345"
        tsname = "ORCL"

        try:
            self.conexion = cx_Oracle.connect(user, passw, host+"/"+tsname)
        except Exception as error:
            print("no se pudo conectar a la nase de datos " + error)
        else:
            print("conexion realizada")
            self.conexion.close()

if __name__ == "__main__":
    nexo = conect()
