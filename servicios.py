import os
import psutil
from tkinter import messagebox
import ctypes, sys
import manejoServicios


def serviciosVer(lista):
    """creacion string servicios seleccionados y validacion"""
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




if __name__ == '__main__':
    pass
