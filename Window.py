from Area import Area
import win32gui


class Window:
    """
    represents a window of an application
    """
    def __init__(self, app_name) -> None:
        self.hwnd = win32gui.FindWindow(None, app_name)

    def resize_and_move_window(self, area: Area):
        """
        resize and move window to given area
        """
        win32gui.MoveWindow(self.hwnd, area.top, area.left,
                            area.width, area.height, True)  # move and resize
        win32gui.SetForegroundWindow(self.hwnd)
