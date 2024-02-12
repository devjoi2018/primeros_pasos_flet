import flet as ft
from pages.dashboard_page.controls.line_chart import LineChart
from pages.dashboard_page.controls.header_control import HeaderControl
from pages.dashboard_page.controls.top_containers import TopContainers
from data.global_memory import GlobalMemory
from theme.theme import Theme
from global_controls.custom_button import CustomButton


class DashboardPage(ft.UserControl):
    def __init__(self, window_width):
        """Pagina del dashboard

        Args:
            window_width (int): Ancho de la ventana
        """
        super().__init__()
        self.window_width = window_width

    def build(self):
        return ft.Container(
            width=self.window_width - GlobalMemory.menu_width,
            padding=ft.Padding(top=50, left=25, right=50, bottom=50),
            content=ft.Column(
                controls=[
                    HeaderControl(),
                    TopContainers(),
                    LineChart(),
                    ft.Container(
                        height=250,
                        width=920,
                        bgcolor=Theme.container_color,
                        padding=25,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        Theme.title_text(
                                            "Your Products",
                                            size=15,
                                        ),
                                        CustomButton(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        name="add",
                                                        color=Theme.principal_text_color,
                                                    ),
                                                    Theme.normal_text(
                                                        "Add Product",
                                                    ),
                                                ],
                                            ),
                                            width=200,
                                        ),
                                    ],
                                ),
                                ft.DataTable(
                                    show_checkbox_column=True,
                                    columns=[
                                        ft.DataColumn(
                                            Theme.subtitle_text("Product"),
                                        ),
                                        ft.DataColumn(
                                            Theme.subtitle_text(
                                                "Performances"),
                                        ),
                                        ft.DataColumn(
                                            Theme.subtitle_text("Stock"),
                                        ),
                                        ft.DataColumn(
                                            Theme.subtitle_text("Price"),
                                        ),
                                        ft.DataColumn(
                                            Theme.subtitle_text("Status"),
                                        ),
                                    ],
                                    rows=[
                                        # TODO: Queda pendiente agregar los datos de la tabla
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
