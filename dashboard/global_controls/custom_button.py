import flet as ft
from theme.theme import Theme


class CustomButton(ft.UserControl):
    def __init__(self, content: ft.Control, width: float, bgcolor: ft.colors = Theme.yellow_color, height: float = 50):
        """Boton personalizado
        """
        super().__init__()
        self.content = content
        self.height = height
        self.width = width
        self.bgcolor = bgcolor

    def build(self):
        return ft.ElevatedButton(
            content=self.content,
            height=self.height,
            width=self.width,
            style=ft.ButtonStyle(
                bgcolor=self.bgcolor,
                overlay_color=ft.colors.TRANSPARENT,
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                        radius=4,
                    ),
                },
            ),
        )
