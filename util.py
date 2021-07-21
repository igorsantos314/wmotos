from module_json import json_ws
import tkinter as tk

class util:

    def __init__(self) -> None:
        pass

    def toCenterScreen(self, width, height):

        root = tk.Tk()

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        root.destroy()
        
        pos_x = float(screen_width)/2 - width/2
        pos_y = float(screen_height)/2 - height/2
        
        if pos_x < 0:
            pos_x = pos_x * -1

        if pos_y < 0:
            pos_y = pos_y * -1

        return f'{width}x{height}+{pos_x:.0f}+{pos_y:.0f}'