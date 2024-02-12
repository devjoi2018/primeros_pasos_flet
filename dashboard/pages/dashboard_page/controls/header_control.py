import flet as ft
from theme.theme import Theme


class HeaderControl(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.title(),
                ft.Row(
                    spacing=20,
                    controls=[
                        self.search_bar(),
                        self.notification(),
                        self.avatar(),
                    ],
                ),
            ],
        )

    def title(self):
        return ft.Column(
            controls=[
                Theme.title_text("Dashboard"),
                Theme.subtitle_text(
                    "Morning John, Welcome to Djournal Dashboard"
                ),
            ],
        )

    def search_bar(self):
        return self.outline_container(
            height=50,
            width=400,
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name="search",
                        color=Theme.disabled_text_color,
                    ),
                    ft.TextField(
                        hint_text="Search here...",
                        border_width=0,
                        cursor_color=Theme.disabled_text_color,
                    ),
                ],
            ),
        )

    def notification(self):
        return self.outline_container(
            height=50,
            width=50,
            content=ft.Icon(
                name="notifications",
                color=Theme.disabled_text_color,
            ),
        )

    def outline_container(self, width: int, height: int, content: ft.Control):
        return ft.Container(
            width=width,
            height=height,
            alignment=ft.alignment.center,
            padding=ft.Padding(left=10, right=10, top=0, bottom=0),
            border=ft.border.all(
                width=1,
                color=Theme.disabled_text_color,
            ),
            content=content,
        )

    def avatar(self):
        return ft.CircleAvatar(
            radius=25,
            foreground_image_url="https://static.vecteezy.com/system/resources/previews/000/457/578/original/set-of-colorful-avatars-of-characters-vector.jpg",
        )
