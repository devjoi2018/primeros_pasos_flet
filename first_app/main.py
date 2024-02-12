import flet as ft
from page.login_page import LoginPage
from controllers.login_controller import LoginController


if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Hello, World!"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.update()

        size = 1200

        login_controller = LoginController(page=page)
        init_page = ft.Container(
            padding=80.0,
            bgcolor=ft.colors.PURPLE,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[
                    ft.colors.PURPLE,
                    ft.colors.RED,
                ],
            ),
            width=size,
            height=700,
            content=LoginPage(size=size, controller=login_controller)
        )

        page.add(init_page)

    ft.app(target=main)
