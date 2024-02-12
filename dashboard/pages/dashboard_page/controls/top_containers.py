import flet as ft
from theme.theme import Theme


class TopContainers(ft.UserControl):
    def __init__(self):
        """Contiene los contenedores superiores del dashboard
        """
        super().__init__()

    def build(self):
        """Construye los contenedores superiores del dashboard

        Returns:
            (ft.Row): Contenedor superior del dashboard
        """
        return ft.Row(
            controls=[
                self.info_top_container(
                    text="Total Stock",
                    value="323.000",
                    src="/images/box.png",
                ),
                self.info_top_container(
                    text="New Orders",
                    value="856",
                    src="/images/list.png",
                ),
                self.info_top_container(
                    text="Paid Orders",
                    value="4.128.000",
                    src="/images/shop.png",
                ),
            ],
        )

    def info_top_container(self, text: str, value: str, src: str):
        """Contenedor base para la informacion superior del dashboard
        como el total de stock, nuevas ordenes, y ordenes pagadas.

        Args:
            text (str): Representa el texto del tipo de informacion
            value (str): Representa el valor

        Returns:
            (ft.Container): Contenedor base
        """
        return ft.Container(
            height=150,
            width=300,
            bgcolor=Theme.container_color,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Image(
                        src=src,
                        height=70,
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            Theme.subtitle_text(text),
                            Theme.normal_text(
                                value=value, text_bold=True,
                            ),
                        ],
                    ),
                ],
            ),
        )
