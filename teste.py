import win32api
import os

path = "{}\\imprimir.txt".format(os.getcwd())
win32api.ShellExecute(0, "print", path, None, ".", 0)