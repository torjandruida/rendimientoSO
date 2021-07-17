import os


import ctypes, sys


def is_admin():
    try:
        print(ctypes.windll.shell32.IsUserAnAdmin())
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def manMem():
    try:
        os.system('cmd /k "wmic computersystem where name="%computername%" set AutomaticManagedPagefile=true"')
        os.system('cmd /k "exit"')
    except:
        print("no ha ejecutado el comando")

def main():
    if is_admin():
        manMem()

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


if __name__ == '__main__':
    main()
