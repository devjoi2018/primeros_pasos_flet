import flet as ft
from global_controls.menu_control import MenuControl
from pages.dashboard_page.dashboard_page import DashboardPage


class HomePage(ft.UserControl):
    def __init__(self, window_height, window_width):
        """Pagina principal de la aplicacion

        Args:
            window_height (int): Altura de la ventana
            window_width (int): Ancho de la ventana
        """
        super().__init__()
        self.window_height = window_height
        self.window_width = window_width

    def build(self):
        return ft.Container(
            content=ft.Row(
                spacing=0,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    MenuControl(window_height=self.window_height),
                    DashboardPage(window_width=self.window_width),
                ],
            ),
        )
