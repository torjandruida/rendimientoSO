import os
import psutil
from tkinter import messagebox
import ctypes, sys
import manejoServicios


def serviciosVer(lista):
    print("entro servicios")
    lst = lista
    if not lst:
        messagebox.showerror("Error", "no ha seleccionado ningun servicio")
    else:
        servSel =""
        for serv in lst:
            servSel += " net Start "+serv+" &"
            try:
                s = psutil.win_service_get(serv)
            except:
                print("el servicio no exite")
            print("estado")
            print(s.status())
        manejoServicios.manServ(servSel)
#servSel =""
#servSel += " net Stop "+key[2]+" &"



if __name__ == '__main__':
    pass
