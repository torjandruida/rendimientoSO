import manejoRegistros

def eleccion(boton):
    print("entro efectos")
    print(boton)
    print(type(boton))
    if boton == 1:
        print("eligio 1")
        manejoRegistros.set_Registro(0,0,0)
    elif boton == 2:
        print("eligio 2")
        manejoRegistros.set_Registro(0,0,0)
    elif boton == 3:
        print("eligio 3")
        manejoRegistros.set_Registro(0,0,0)


if __name__ == '__main__':
    pass
