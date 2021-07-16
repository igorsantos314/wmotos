import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "sqlite3"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="OficeSystem",
    version="1.0",
    description="Sistema para Gerenciar Oficina",
    options={"build_exe": build_exe_options},
    executables=[Executable("App.py", base=base, icon="igtec_icon.ico")]
)