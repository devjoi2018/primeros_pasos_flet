import flet as ft
from pages.note_app_page.note_app_page import NoteAppPage


class Main:
    def __init__(self):
        super().__init__()

    def main(self, page: ft.Page):
        page.title = "Note App"
        page.update()

        app = NoteAppPage(
            window_height=page.window_height,
            window_width=page.window_width,
        )

        page.add(app)


if __name__ == "__main__":
    ft.app(target=Main().main)
