import flet as ft
from global_controls.custom_divider import CustomDivider
from controllers.login_controller import LoginController
from global_controls.custom_button import CustomButton


class LoginPage(ft.UserControl):
    def __init__(self, size, controller: LoginController):
        super().__init__()
        self.size = size
        self.controller = controller

    def build(self):

        custom_divider = CustomDivider(color=ft.colors.WHITE, height=2.0,)
        login_button = CustomButton(
            on_click=self.controller.login_button_clicked,
            width=450,
            content=ft.Text("Submit", weight=ft.FontWeight.BOLD),
        )

        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.left_content(custom_divider=custom_divider),
                self.right_content(custom_button=login_button),
            ],
        )

    # Metodo que contiene todo el cuerpo izquierdo de la pantalla
    def left_content(self, custom_divider):
        return ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.Container(
                    width=50.0,
                    height=50.0,
                    bgcolor=ft.colors.WHITE,
                    image_src=f"images/logo.png"
                ),
                ft.Text(
                    value="Welcome!",
                    color=ft.colors.WHITE,
                    size=60.0,
                    weight=ft.FontWeight.BOLD,
                ),
                custom_divider,
                ft.Container(
                    width=self.size / 2,
                    content=ft.Text(
                        value="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean euismod bibendum laoreet. Proin gravida dolor sit amet lacus accumsan et viverra justo commodo.",
                        color=ft.colors.WHITE,
                    ),
                ),
                ft.ElevatedButton(
                    content=ft.Text("Learn more"),
                    on_click=self.controller.button_clicked,
                ),
            ],
        )

    # Metodo que contiene todo el cuerpo derecho de la pantalla
    def right_content(self, custom_button: CustomButton):
        return ft.Container(
            bgcolor="#FFFFFF,0.2",
            height=450,
            expand=True,
            padding=20.0,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    ft.Text(
                        "Sign in",
                        size=40.0,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                "User Name",
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.LEFT,
                                width=450,
                                weight=ft.FontWeight.BOLD,
                            ),
                            self.custom_text_field(hint_text="Your name"),
                        ],
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                "Password",
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.LEFT,
                                width=450,
                                weight=ft.FontWeight.BOLD,
                            ),
                            self.custom_text_field(
                                hint_text="Your password", password=True,
                            ),
                        ],
                    ),
                    custom_button,
                ],
            ),
        )

    # Control personalizado para los inputs de texto
    def custom_text_field(self, hint_text: str, border_radius: float = 50.0, password: bool = False):
        return ft.TextField(
            hint_text=hint_text,
            border_radius=border_radius,
            password=password,
            bgcolor="#FFFFFF,0.2",
            border_color=ft.colors.TRANSPARENT,
            height=50.0,
        )
