import manejoRegistros

def eleccion(boton):

    """creacion string registros para y validacion de la seleccion para seleccionar la ejecucion"""
    print("entro efectos")
    print(boton)
    print(type(boton))
    path1 = "SOFTWARE\\Microsoft\\windows\\CurrentVersion\\Explorer\\VisualEffects"
    path2 = "Control Panel\\Desktop"

    reg1 = "VisualFXSetting"
    reg2 = "UserPreferencesMask"

    val1 = b'\x9E\x1E\x07\x80\x12\x00\x00\x00'
    val2 = b'\x9E\x3E\x07\x80\x12\x00\x00\x00'
    val3 = b'\x90\x12\x03\x80\x10\x00\x00\x00'

    if boton == 1:
        print("eligio 1")
        manejoRegistros.set_Registro(path1,reg1,0)
        manejoRegistros.set_Registro(path2,reg2,val1)
    elif boton == 2:
        print("eligio 2")
        manejoRegistros.set_Registro(path1,reg1,1)
        manejoRegistros.set_Registro(path2,reg2,val2)
    elif boton == 3:
        print("eligio 3")
        manejoRegistros.set_Registro(path1,reg1,2)
        manejoRegistros.set_Registro(path2,reg2,val3)


if __name__ == '__main__':
    pass
