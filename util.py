from module_json import json_ws

class util:

    def __init__(self) -> None:
        pass

    def toCenterScreen(self, width, height):
        pos_x = float(json_ws().getWidthScreen())/2 - width/2
        pos_y = float(json_ws().getHeightScreen())/2 - height/2
        
        if pos_x < 0:
            pos_x = pos_x * -1

        if pos_y < 0:
            pos_y = pos_y * -1

        return f'{width}x{height}+{pos_x:.0f}+{pos_y:.0f}'