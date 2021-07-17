from tkinter import *
import platform
import efectosVisuales


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

            button2 = Button(miFrame2,text = "aplicar efectos", width = "20",height = "10", font = "none 10 bold", command=lambda: efectosVisuales.eleccion(menuBoton1) )
            button2.pack(side= LEFT, padx=15, pady=20)

            button3 = Button(miFrame2,text = "reiniciar", width = "20",height = "10", font = "none 10 bold")
            button3.pack(side= RIGHT, padx=15, pady=20)






    def memoVi():
        miFrame3.pack()
        miFrame2.pack_forget()
        miFrame4.pack_forget()
        miFrame3.config(bg = "yellow")
        miFrame3.config(width = "650",height = "350")
        miFrame.destroy()

    def serv():
        miFrame4.pack()
        miFrame2.pack_forget()
        miFrame3.pack_forget()
        miFrame4.config(bg = "black")
        miFrame4.config(width = "650",height = "350")
        miFrame.destroy()

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
