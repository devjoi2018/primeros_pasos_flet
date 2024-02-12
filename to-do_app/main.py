import flet as ft
from todo_app import TodoApp


class Main:
    def __init__(self):
        super().__init__()

    def main(self, page: ft.Page):
        page.title = "Todo App"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.update()

        todo = TodoApp()

        page.add(todo)


if __name__ == "__main__":
    ft.app(target=Main().main)
