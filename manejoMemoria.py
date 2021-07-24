import os
from psutil import virtual_memory
import psutil
import math
import ctypes, sys
from tkinter import messagebox

mem = virtual_memory()
disk_usage = psutil.disk_usage("C:\\")

myRoundNumber = math.ceil(mem.total/1024/1024/1024)
ddlibre = int(math.ceil(disk_usage.free/1024/1024/1024))
minimo = str(myRoundNumber*1024)
maximo = str(myRoundNumber*1024*2)
ddMin = int(30 + (myRoundNumber*2))
sizeMem = 'wmic pagefileset where name="C:\\\pagefile.sys" set InitialSize='+minimo+', MaximumSize='+maximo




def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()

    except:
        return False

def chanMem(opc):

    print("entro")


    if opc == 1:
        try:
            os.system('cmd /k "wmic computersystem where name="%computername%" set AutomaticManagedPagefile=true"')

        except:
            print("no ha ejecutado el comando")

    elif opc ==2:
        if ddMin < ddlibre :
            try:
                print("entro4")
                os.system('cmd /k "wmic pagefile list /format:list & wmic computersystem where name="%computername%" set AutomaticManagedPagefile=false & '+sizeMem+'"')

            except:
                print("no ha ejecutado el comando")

        else:
            messagebox.showerror("Error", "el sistema no tiene espacio suficiente")

    elif opc ==3:
        try:
            os.system('cmd /k "wmic pagefile list /format:list & wmic computersystem where name="%computername%" set AutomaticManagedPagefile=false & wmic pagefileset where name="C:\\\pagefile.sys" delete"')

        except:
            print("no ha ejecutado el comando")

def manMem(opcbtn):

    if is_admin():
        chanMem(opcbtn)

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


if __name__ == '__main__':
    pass
