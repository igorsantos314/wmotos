import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": [
    "tkinter", 
    "sqlite3",
    "pylab",
    "numpy",
    "win32api",
    "matplotlib.pyplot",
    "Tela_Backup_BD", 
    "Tela_Config", 
    "Tela_Contabilidade", 
    "Tela_Menu_Principal",
    "Tela_Show_OS",
    "Tela_Cadastrar_OS",
    "Tela_Editar_OS",
    "Tela_Cadastrar_Produto",
    "Tela_Editar_Produto",
    "Tela_Vender_Produtos",
    "Tela_Plot_Graficos",
    "util",
    "module_json",
    "module_print",
    "Persistencia",
    "IGTEC"
    ]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="IGTEC - Ordem de Serviço",
    version="2.0.5",
    description="Sistema para Gerenciar Oficina",
    options={"build_exe": build_exe_options},
    executables=[Executable("IGTEC.py", base=base, icon="igtec_icon.ico")]
)