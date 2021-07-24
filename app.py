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
    raiz = Tk()

    def efecVis():
        global ventCont1
        ventCont1 += 1
        miFrame2.pack()
        miFrame3.pack_forget()
        miFrame4.pack_forget()
        miFrame2.config(bg = "green")
        miFrame2.config(width = "650",height = "350")
        miFrame.destroy()

        if ventCont1 == 1:


            def sel():
               selection = "You selected the option " + str(var.get())
               global menuBoton1
               menuBoton1 = var.get()
               label.config(text = selection)



            var = IntVar()
            R1 = Radiobutton(miFrame2, text="dejar que windows elija", variable=var, value=1,font = "none 10 bold", command = sel)
            R1.pack(side = TOP,padx=15, pady=30)

            R2 = Radiobutton(miFrame2, text="calidad de graficos", variable=var, value=2,font = "none 10 bold", command = sel)
            R2.pack(side = TOP, padx=15, pady=30)

            R3 = Radiobutton(miFrame2, text="rendimiento de graficos", variable=var, value=3,font = "none 10 bold", command = sel)
            R3.pack(side = TOP, padx=15, pady=30)

            label = Label(miFrame2)
            label.pack()

            button1 = Button(miFrame2,text = "aplicar efectos", width = "20",height = "10", font = "none 10 bold",
                                            command=lambda: efectosVisuales.eleccion(menuBoton1) )
            button1.pack(side= LEFT, padx=15, pady=20)

            button2 = Button(miFrame2,text = "reiniciar", width = "20",height = "10", font = "none 10 bold",
                                            command=lambda: subprocess.run("shutdown -r"))
            button2.pack(side= RIGHT, padx=15, pady=20)






    def memoVi():
        global ventCont2
        ventCont2 += 1
        miFrame3.pack()
        miFrame2.pack_forget()
        miFrame4.pack_forget()
        miFrame3.config(bg = "yellow")
        miFrame3.config(width = "650",height = "350")
        miFrame.destroy()

        if ventCont2 == 1:
            def sel():
               selection = "You selected the option " + str(var.get())
               global menuBoton2
               menuBoton2 = var.get()
               label.config(text = selection)



            var = IntVar()
            R4 = Radiobutton(miFrame3, text="administrado por windows", variable=var, value=1,font = "none 10 bold", command = sel)
            R4.pack(side = TOP,padx=15, pady=30)

            R5 = Radiobutton(miFrame3, text="mejor rendimiento", variable=var, value=2,font = "none 10 bold", command = sel)
            R5.pack(side = TOP, padx=15, pady=30)

            R6 = Radiobutton(miFrame3, text="sin paginación", variable=var, value=3,font = "none 10 bold", command = sel)
            R6.pack(side = TOP, padx=15, pady=30)

            label = Label(miFrame3)
            label.pack()

            button3 = Button(miFrame3,text = "aplicar memoria", width = "15",height = "1", font = "none 10 bold",
                                            command=lambda: manejoMemoria.manMem(menuBoton2))
            button3.pack(side= LEFT, padx=15, pady=20)

            button4 = Button(miFrame3,text = "reiniciar", width = "15",height = "1", font = "none 10 bold",
                                            command=lambda: subprocess.run("shutdown -r"))
            button4.pack(side= RIGHT, padx=15, pady=20)


    def serv():
        global ventCont3
        ventCont3 += 1
        miFrame4.pack()
        miFrame2.pack_forget()
        miFrame3.pack_forget()
        miFrame4.config(bg = "black")
        miFrame4.config(width = "650",height = "350")
        miFrame.destroy()

        if ventCont3 == 1:

            intvar_dict = {}

            checkbutton_list = []
            seleccion_list = []

            def seleccion():

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

            for filename in basDat.fetchData():

                intvar_dict[filename] = IntVar()

                c = Checkbutton(miFrame4, text=filename[1], variable=intvar_dict[filename])
                c.grid(sticky=W,row=filename[0], column=0)

                checkbutton_list.append(c)
                label = Label(miFrame4,text=filename[3])
                label.config(height=1, width=73)
                label.grid(sticky=W,row=filename[0], column=1)

            numCol = (len(basDat.fetchData()))

            label = Label(miFrame4,text="")
            label.config(height=1, width=3)

            label.grid(row=numCol+1, column=0)
            label.grid(row=numCol+1, column=1)

            button5 = Button(miFrame4,text = "aplicar memoria", width = "15",height = "1", font = "none 10 bold",
                                            command = seleccion)
            button5.grid(row=numCol+2, column=1 )





    raiz.title("PRIH "+"Sistema Operativo "+platform.system()+" "+platform.release())
    raiz.resizable(False,False)
    raiz.geometry("650x350")
    raiz.config(bg = "blue")

    miFrame = Frame()
    miFrame.pack()
    miFrame.config(bg = "red")
    miFrame.config(width = "650",height = "350")

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

        button = Button(miFrame,text = "Salir", width = "10",height = "1", font = "none 10 bold",command= miFrame.quit)
        button.pack(side= BOTTOM, padx=15, pady=20)
        miLabel2 = Label(miFrame, text = "Su sistema operativo no es compatible",font = "none 14 bold",anchor = CENTER,width = "650",height = "350",bg = "red")
        miLabel2.pack()

    raiz.mainloop()

if __name__ == "__main__":
    main()
