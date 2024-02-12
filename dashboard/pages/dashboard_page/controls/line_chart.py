import flet as ft
from theme.theme import Theme


class LineChart(ft.UserControl):
    def __init__(self):
        """Grafico de linea
        """
        super().__init__()

    def build(self):
        return ft.Container(
            height=400,
            width=920,
            bgcolor=Theme.container_color,
            padding=25,
            content=ft.LineChart(
                data_series=self.line_data(),
                border=ft.Border(
                    top=ft.BorderSide(
                        color=ft.colors.with_opacity(
                            0.2, ft.colors.ON_SURFACE),
                        width=3,
                    ),
                    bottom=ft.BorderSide(
                        color=ft.colors.with_opacity(
                            0.2, ft.colors.ON_SURFACE),
                        width=3,
                    ),
                    left=None,
                    right=None,
                ),
                horizontal_grid_lines=ft.ChartGridLines(
                    dash_pattern=[10, 14],
                    interval=1,
                    color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE),
                    width=3,
                ),
                left_axis=ft.ChartAxis(
                    labels=self.left_axis(),
                    labels_size=100,
                ),
                bottom_axis=ft.ChartAxis(
                    labels=self.add_labels(),
                    labels_size=35,
                ),
                tooltip_bgcolor=ft.colors.with_opacity(
                    0.8, ft.colors.BLUE_GREY),
                min_y=0,
                max_y=3,
                min_x=0,
                max_x=11,
                # animate=5000,
                expand=True,
            )
        )

    def line_data(self):
        """Funcion que agrega los datos que generan la curva de la grafica

        Returns:
            (list): Lista de datos de la grafica
        """
        return [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(0, 1.2),
                    ft.LineChartDataPoint(2.6, 2),
                    ft.LineChartDataPoint(4.9, 1),
                    ft.LineChartDataPoint(6.8, 2.1),
                    ft.LineChartDataPoint(8, 1),
                    ft.LineChartDataPoint(9.5, 2.9),
                    ft.LineChartDataPoint(11, 2.8),
                ],
                stroke_width=5,
                color=ft.colors.CYAN,
                curved=True,
                stroke_cap_round=True,
            )
        ]

    def left_axis(self):
        """Funcion que agrega los valores del eje izquierdo

        Returns:
            (list): Lista de valores del eje izquierdo
        """
        list_of_values = [
            "50.000",
            "150.000",
            "300.000",
            "500.000",
        ]
        left_axis_model = []

        for index, value in enumerate(list_of_values):
            left_axis_model.append(
                ft.ChartAxisLabel(
                    value=index,
                    label=ft.Text(
                        value=value,
                        size=12,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
            )

        return left_axis_model

    def add_labels(self):
        """Funcion que agrega las etiquetas del eje inferior

        Returns:
            (list): Lista de etiquetas del eje inferior
        """
        list_of_months = [
            "JAN",
            "FEB",
            "MAR",
            "APR",
            "MAY",
            "JUN",
            "JUL",
            "AGO",
            "SEP",
            "OCT",
            "NOV",
            "DEC",
        ]
        labels = []

        for index, month in enumerate(list_of_months):
            labels.append(
                ft.ChartAxisLabel(
                    value=index,
                    label=ft.Container(
                        ft.Text(
                            value=month,
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(
                                0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            )
        return labels
