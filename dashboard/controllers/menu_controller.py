import flet as ft
from theme.theme import Theme


class MenuController:
    def __init__(self, update_callback=None):
        """Controlador que se encarga de manejar la logica del menu lateral
        """
        super().__init__()
        self.menu_items = [
            {"name": "Dashboard", "icon_name": "view_comfy_alt", "is_selected": True},
            {"name": "Product", "icon_name": "inventory_2", "is_selected": False},
            {"name": "Transaction", "icon_name": "description", "is_selected": False},
            {"name": "Analytics", "icon_name": "pie_chart", "is_selected": False},
            {"name": "Customer", "icon_name": "group", "is_selected": False},
            {"name": "Settings", "icon_name": "settings", "is_selected": False},
        ]
        self.update_callback = update_callback

    def on_hover(self, e):
        """Funcion que se ejecuta cuando el mouse esta encima de un item del menu

        Args:
            e (Event): Evento de mouse
        """

        e.control.bgcolor = Theme.bg_color if e.data == "true" else Theme.bg_menu_color
        e.control.update()

    def on_click(self, e):
        """Funcion que se ejecuta cuando se hace click en un item del menu

        Args:
            e (Event): Evento de click
        """
        for item in self.menu_items:
            item["is_selected"] = item["name"] == e.control.content.controls[0].controls[1].value
        if self.update_callback:
            self.update_callback()  # Llama a la función de callback después de la actualización
