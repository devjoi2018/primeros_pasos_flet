import flet as ft
from pages.home_page.home_page import HomePage
from theme.theme import Theme


class Main:
    def __init__(self):
        super().__init__()

    def main(self, page: ft.Page):
        page.title = "Dashboard"
        page.bgcolor = Theme.bg_colorc
        page.on_resize = self.on_resize
        page.padding = 0
        page.window_height = 1024
        page.window_width = 1609
        page.update()

        _dashboard_page = HomePage(
            window_height=page.window_height,
            window_width=page.window_width,
        )

        page.add(_dashboard_page)

    def on_resize(self, e):
        """Funcion que se ejecuta cuando se redimensiona la ventana

        Args:
            e (Event): Evento de redimensionamiento
        """
        page = e.page
        page.clean()
        _dashboard_page = HomePage(
            window_height=page.window_height,
            window_width=page.window_width,
        )
        page.add(_dashboard_page)


if __name__ == "__main__":
    ft.app(target=Main().main)
