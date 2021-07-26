import sys

import os
import psutil

import ctypes, sys



def is_admin():
    """validacion del tipo de usuario"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()

    except:
        return False

def chanServ(opc):
    """apagado de servicios seleccionados"""
    try:
        print("entro")
        os.system('cmd /k "'+opc+' exit"')


    except:
        print("no ha ejecutado el comando")

def quit():
    global root
    root.quit()


def manServ(opcbtn):
    """elevacion a usuario administrador"""
    if is_admin():
        chanServ(opcbtn)

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)


if __name__ == '__main__':
    pass
