import os
from psutil import virtual_memory
import psutil
import math
import ctypes, sys
from tkinter import messagebox

"""verificacion de la memoria libre del disco duro"""
mem = virtual_memory()
disk_usage = psutil.disk_usage("C:\\")
myRoundNumber = math.ceil(mem.total/1024/1024/1024)
ddlibre = int(math.ceil(disk_usage.free/1024/1024/1024))
minimo = str(myRoundNumber*1024)
maximo = str(myRoundNumber*1024*2)
ddMin = int(30 + (myRoundNumber*2))
sizeMem = 'wmic pagefileset where name="C:\\\pagefile.sys" set InitialSize='+minimo+', MaximumSize='+maximo



def is_admin():
    """validacion del tipo de usuario"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()

    except:
        return False

def chanMem(opc):
    """validacion de la opcion de memoria elegida y ejecucion de acuerdo a la opcion seleccionada"""
    print("entro")


    if opc == 1:
        """seleccion de memoria manejada automaticamente por el sistema operativo"""
        try:
            os.system('cmd /k "wmic computersystem where name="%computername%" set AutomaticManagedPagefile=true"')

        except:
            print("no ha ejecutado el comando")

    elif opc ==2:
        """validacion de espacio en disco duro y seleccion de rendimiento"""
        if ddMin < ddlibre :
            try:
                print("entro4")
                os.system('cmd /k "wmic pagefile list /format:list & wmic computersystem where name="%computername%" set AutomaticManagedPagefile=false & '+sizeMem+'"')

            except:
                print("no ha ejecutado el comando")

        else:
            messagebox.showerror("Error", "el sistema no tiene espacio suficiente")

    elif opc ==3:
        """seleccion de trabajo sin memoria virtual"""
        try:
            os.system('cmd /k "wmic pagefile list /format:list & wmic computersystem where name="%computername%" set AutomaticManagedPagefile=false & wmic pagefileset where name="C:\\\pagefile.sys" delete"')

        except:
            print("no ha ejecutado el comando")

def manMem(opcbtn):
    """elevacion a usuario administrador"""
    if is_admin():
        chanMem(opcbtn)

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


if __name__ == '__main__':
    pass
