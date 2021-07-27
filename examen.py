from tkinter import *
from tkinter import ttk
import platform
import subprocess
import efectosVisuales
import manejoMemoria
import servicios
import basDat



ventCont1 = 0
ventCont2 = 0
ventCont3 = 0

menuBoton1 = ""

def main():
    """Creacion de la ventana"""
    raiz = Tk()

    def efecVis():
        """Frame para el manejo del Frame1 efectos visuales"""
        global ventCont1
        ventCont1 += 1
        miFrame2.pack()
        miFrame3.pack_forget()
        miFrame4.pack_forget()
        miFrame2.config(bg = "green")
        miFrame2.config(width = "1075",height = "350")
        miFrame.destroy()

        if ventCont1 == 1:


            def sel():
               """verificador de seleccion de los Radiobutton del frame1"""
               selection = " ha seleccionado la opcion " + str(var.get())
               global menuBoton1
               menuBoton1 = var.get()
               label.config(text = selection)


            """creacion de los Radiobutton del frame1"""
            var = IntVar()
            R1 = Radiobutton(miFrame2, text="dejar que windows elija", variable=var, value=1,font = "none 10 bold", command = sel)
            R1.pack(side = TOP,padx=15, pady=30)

            R2 = Radiobutton(miFrame2, text="calidad de graficos", variable=var, value=2,font = "none 10 bold", command = sel)
            R2.pack(side = TOP, padx=15, pady=30)

            R3 = Radiobutton(miFrame2, text="rendimiento de graficos", variable=var, value=3,font = "none 10 bold", command = sel)
            R3.pack(side = TOP, padx=15, pady=30)

            label = Label(miFrame2)
            label.pack()

            """creacion de los botones frame1"""
            button1 = Button(miFrame2,text = "aplicar efectos", width = "20",height = "1", font = "none 10 bold",
                                            command=lambda: efectosVisuales.eleccion(menuBoton1) )
            button1.pack(side= LEFT, padx=15, pady=20)

            button2 = Button(miFrame2,text = "reiniciar", width = "20",height = "1", font = "none 10 bold",
                                            command=lambda: subprocess.run("shutdown -r"))
            button2.pack(side= RIGHT, padx=15, pady=20)






    def memoVi():
        """Frame para el manejo del Frame2 memoria virtual"""

        global ventCont2
        ventCont2 += 1
        miFrame3.pack()
        miFrame2.pack_forget()
        miFrame4.pack_forget()
        miFrame3.config(bg = "yellow")
        miFrame3.config(width = "1075",height = "500")
        miFrame.destroy()

        if ventCont2 == 1:
            def sel():
               """verificador de seleccion de los Radiobutton del frame2"""
               selection = "You selected the option " + str(var.get())
               global menuBoton2
               menuBoton2 = var.get()
               label.config(text = selection)


            """creacion de los Radiobutton del frame2"""
            var = IntVar()
            R4 = Radiobutton(miFrame3, text="administrado por windows", variable=var, value=1,font = "none 10 bold", command = sel)
            R4.pack(side = TOP,padx=15, pady=30)

            R5 = Radiobutton(miFrame3, text="mejor rendimiento", variable=var, value=2,font = "none 10 bold", command = sel)
            R5.pack(side = TOP, padx=15, pady=30)

            R6 = Radiobutton(miFrame3, text="sin paginación", variable=var, value=3,font = "none 10 bold", command = sel)
            R6.pack(side = TOP, padx=15, pady=30)

            label = Label(miFrame3)
            label.pack()

            """creacion de los botones frame2"""
            button3 = Button(miFrame3,text = "aplicar memoria", width = "15",height = "1", font = "none 10 bold",
                                            command=lambda: manejoMemoria.manMem(menuBoton2))
            button3.pack(side= LEFT, padx=15, pady=20)

            button4 = Button(miFrame3,text = "reiniciar", width = "15",height = "1", font = "none 10 bold",
                                            command=lambda: subprocess.run("shutdown -r"))
            button4.pack(side= RIGHT, padx=15, pady=20)


    def serv():
        """Frame para el manejo del Frame3 servicios"""
        global ventCont3
        ventCont3 += 1
        miFrame4.pack()
        miFrame2.pack_forget()
        miFrame3.pack_forget()
        miFrame4.config(bg = "black")
        miFrame4.config(width = "1075",height = "500")
        miFrame.destroy()

        if ventCont3 == 1:

            intvar_dict = {}

            checkbutton_list = []
            seleccion_list = []

            def seleccion():
                """verificador de seleccion de los Checkbutton del frame3"""
                for key, value in intvar_dict.items():
                    if value.get() > 0:
                        print('seleccionada:', key[2])
                        seleccion_list.append(key[2])

                servicios.serviciosVer(seleccion_list)
                seleccion_list.clear()

            intvar_dict.clear()


            for cb in checkbutton_list:
                cb.destroy()
                checkbutton_list.clear()


            """creacion de los Chekbutton y labels del frame2"""
            for filename in basDat.fetchData():

                intvar_dict[filename] = IntVar()

                c = Checkbutton(miFrame4, text=filename[1], variable=intvar_dict[filename])
                c.grid(sticky=W,row=filename[0], column=0)

                checkbutton_list.append(c)
                label = Label(miFrame4,text=filename[3], justify=LEFT)
                label.config(height=1, width=106)
                label.grid(sticky=S, row=filename[0], column=1)

            numCol = (len(basDat.fetchData()))

            label = Label(miFrame4,text="")
            label.config(height=1, width=3)

            label.grid(row=numCol+1, column=0)
            label.grid(row=numCol+1, column=1)

            """creacion del boton frame3"""
            button5 = Button(miFrame4,text = "apagar servicios seleccionados", width = "15",height = "1", font = "none 10 bold",
                                            command = seleccion)
            button5.grid(row=numCol+2, column=1 )




    """configuracion de la ventana"""
    raiz.title("PRIH "+"Sistema Operativo "+platform.system()+" "+platform.release())
    raiz.resizable(True,True)
    raiz.geometry("1075x500")
    raiz.config(bg = "blue")

    """configuracion frame0"""
    miFrame = Frame()
    miFrame.pack()
    miFrame.config(bg = "red")
    miFrame.config(width = "1075",height = "500")

    """validacion del sistema operativo"""
    if platform.system() == "Windows" and platform.release() == "10":
        barraMenu = Menu(raiz)
        barraMenu.add_command(label = "Efectos visuales", command=efecVis)
        barraMenu.add_command(label = "memoria virtual", command=memoVi)
        barraMenu.add_command(label = "servicios", command=serv)
        barraMenu.add_command(label = "salir", command=raiz.destroy)
        raiz.config(menu = barraMenu)


        miFrame2 = Frame()
        miFrame3 = Frame()
        miFrame4 = Frame()

    else:
        """creacion boton salir cuando el sistema operativo es erroneo"""
        button = Button(miFrame,text = "Salir", width = "10",height = "1", font = "none 10 bold",command= miFrame.quit)
        button.pack(side= BOTTOM, padx=15, pady=20)
        miLabel2 = Label(miFrame, text = "Su sistema operativo no es compatible",font = "none 14 bold",anchor = CENTER,width = "1075",height = "500",bg = "red")
        miLabel2.pack()

    raiz.mainloop()

if __name__ == "__main__":
    main()
