import winreg
import ctypes


"""
def set_Registro(path,nombre,valor):
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, "SOFTWARE\\Microsoft\\windows\\CurrentVersion\\Explorer\\VisualEffects", 0,winreg.KEY_ALL_ACCESS) as sub_key:
            existing_path_value = winreg.EnumValue(sub_key,0)
            #winreg.SetValueEx(sub_key, "prueba", 0, winreg.REG_DWORD, 1)
            #winreg.SetValueEx(sub_key, "VisualFXSetting", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(sub_key)
            print(type(sub_key))
            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x1A

            SMTO_ABORTIFHUNG = 0x0002

            result = ctypes.c_long()
            SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
            SendMessageTimeoutW(
                HWND_BROADCAST,
                WM_SETTINGCHANGE,
                0,
                u"Environment",
                SMTO_ABORTIFHUNG,
                5000,
                ctypes.byref(result))

            print(f"{existing_path_value}")
            print(type(existing_path_value))
"""
def set_Registro(path,nombre,valor):
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, "Control Panel\\Desktop", 0,winreg.KEY_ALL_ACCESS) as sub_key:
            existing_path_value = winreg.EnumValue(sub_key,39)
            #winreg.SetValueEx(sub_key, "prueba", 0, winreg.REG_BINARY, b'\x90\x12\x03\x80\x10\x00\x00\x22')
            #winreg.SetValueEx(sub_key, "VisualFXSetting", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(sub_key)
            print(type(sub_key))
            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x1A

            SMTO_ABORTIFHUNG = 0x0002

            result = ctypes.c_long()
            SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
            SendMessageTimeoutW(
                HWND_BROADCAST,
                WM_SETTINGCHANGE,
                0,
                u"Environment",
                SMTO_ABORTIFHUNG,
                5000,
                ctypes.byref(result))

            print(f"{existing_path_value}")
            print(type(existing_path_value))



if __name__ == "__main__":
    set_Registro(0,0,0)
    pass
