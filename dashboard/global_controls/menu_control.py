from theme.theme import Theme
import flet as ft
from data.global_memory import GlobalMemory
from global_controls.custom_button import CustomButton
from controllers.menu_controller import MenuController


class MenuControl(ft.UserControl):
    def __init__(self, window_height):
        """Menu lateral izquierdo de la aplicacion

        Args:
            window_height (int): Altura de la ventana
        """
        super().__init__()
        self.window_height = window_height
        self.menu_controller = MenuController(update_callback=self.update_ui)

    global menu_width
    menu_width = GlobalMemory.menu_width

    def update_ui(self):
        """Actualiza la UI del menú para reflejar los cambios."""
        self.controls.clear()  # Opcionalmente, limpia los controles existentes si es necesario
        # Reconstruye la interfaz de usuario
        self.controls.append(self.build())
        self.update()  # Solicita la actualización de la interfaz de usuario

    def build(self):
        return ft.Container(
            padding=ft.Padding(top=50, left=0, right=0, bottom=50),
            bgcolor=Theme.bg_menu_color,
            width=menu_width,
            height=self.window_height,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.logo_and_items(),
                    self.upgrade_now(),
                ],
            ),
        )

    # region [Methods]
    def logo_and_items(self):
        """Logo y items del menu lateral

        Returns:
            (ft.Column): Columna con el logo y los items del menu lateral
        """
        control = [
            ft.CircleAvatar(
                radius=102,
                height=102,
                bgcolor=ft.colors.WHITE,
                content=ft.CircleAvatar(
                    height=100,
                    radius=100,
                    foreground_image_url="https://th.bing.com/th/id/OIG.y57kODYtU8QWJOZYUJye?w=1024&h=1024&rs=1&pid=ImgDetMain"
                ),
            ),
            Theme.normal_text("Djournal"),
            ft.Container(height=30),
        ]

        for item in self.menu_controller.menu_items:
            control.append(
                self.menu_item(
                    icon_name=item["icon_name"],
                    text=item["name"],
                    is_selected=item["is_selected"],
                )
            )

        return ft.Column(
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=control
        )

    def menu_item(self, icon_name: str, text: str, is_selected: bool):
        """Modelo del item del menu lateral

        Args:
            icon_name (str): Nombre del icono del item
            text (str): Texto a mostrar en el item
            is_selected (bool, optional): Indica si el item esta seleccionado. Por defecto tiene un valor False.

        Returns:
            _type_: _description_
        """
        return ft.Container(
            bgcolor=Theme.bg_menu_color if not is_selected else Theme.bg_color,
            height=50,
            width=menu_width,
            on_click=self.menu_controller.on_click,
            on_hover=self.menu_controller.on_hover if not is_selected else None,
            padding=ft.Padding(left=25, right=0, top=0, bottom=0),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(
                                name=icon_name, color=Theme.principal_text_color if is_selected else Theme.disabled_text_color
                            ),
                            Theme.normal_text(
                                text) if is_selected else Theme.subtitle_text(text),
                        ],
                    ),
                    ft.Container(
                        visible=is_selected if is_selected else False,
                        height=50,
                        width=5,
                        bgcolor=Theme.yellow_color,
                    ),
                ],
            ),
        )

    def upgrade_now(self):
        """Contenedor con el boton para actualizar a la version PRO

        Returns:
            (ft.Container): Contenedor con el boton para actualizar a la version PRO (ft.Container
        """
        return ft.Container(
            height=300,
            width=menu_width,
            bgcolor=Theme.bg_color,
            margin=25,
            padding=20,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        border_radius=10,
                        height=100,
                        width=100,
                        src=f"images/logo.png",
                    ),
                    Theme.title_text("Discover Pro", size=15),
                    ft.Text(
                        "Unlock for information now upgrade to ",
                        color=Theme.disabled_text_color,
                        spans=[
                            ft.TextSpan(
                                text="PRO",
                                style=ft.TextStyle(
                                    weight=ft.FontWeight.BOLD,
                                    color=Theme.principal_text_color,
                                ),
                            ),
                        ],
                        text_align=ft.TextAlign.CENTER,
                    ),
                    CustomButton(
                        content=Theme.normal_text("Upgrade Now"),
                        width=menu_width,
                        bgcolor=Theme.yellow_color,
                    ),
                ],
            ),
        )
    # endregion [Methods]
