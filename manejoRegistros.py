import winreg
import ctypes



def set_Registro(path,nombre,valor):
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, path, 0,winreg.KEY_ALL_ACCESS) as sub_key:
            existing_path_value = winreg.EnumValue(sub_key,0)
            if nombre == "VisualFXSetting":
                winreg.SetValueEx(sub_key, "VisualFXSetting", 0, winreg.REG_DWORD, valor)
            elif nombre == "UserPreferencesMask" :
                winreg.SetValueEx(sub_key, "UserPreferencesMask", 0, winreg.REG_BINARY, valor)
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
    pass
