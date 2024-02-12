import flet as ft
from Task import Task


class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(
            hint_text="Que necesitas hacer?", expand=True
        )
        self.task = ft.Column()

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todas"),
                ft.Tab(text="Activas"),
                ft.Tab(text="Completas"),
            ]
        )

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.task,
                    ],
                ),
            ],
        )

    def tabs_changed(self, e):
        self.update()

    def add_clicked(self, e):
        task = Task(
            self.new_task.value,
            self.task_delete,
            self.tabs_changed
        )
        self.task.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.task.controls.remove(task)
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.task.controls:
            task.visible = (status == "Todas"
                            or (status == "Activas" and task.completed == False)
                            or (status == "Completas" and task.completed))
        super().update()
