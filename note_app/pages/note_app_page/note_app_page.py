import flet as ft


class NoteAppPage(ft.UserControl):
    def __init__(self, window_height, window_width):
        super().__init__()
        self.window_height = window_height
        self.window_width = window_width

    def build(self):
        return ft.Text(f"Alto de la ventana {self.window_height}, y ancho {self.window_width}")
