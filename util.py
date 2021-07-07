class util:

    def __init__(self) -> None:
        pass

    def toCenterScreen(self, width, height):
        pos_x = 1900/2 - width/2
        pos_y = 1200/2 - height/2
        
        if pos_x < 0:
            pos_x = pos_x * -1

        if pos_y < 0:
            pos_y = pos_y * -1

        return f'{width}x{height}+{pos_x:.0f}+{pos_y:.0f}'