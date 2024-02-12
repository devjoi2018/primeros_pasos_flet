from flet import (
    Container,
    UserControl,
    LinearGradient,
    alignment,
    colors,
)


class CustomButton(UserControl):
    def __init__(self, on_click, content, width=100.0, height=50.0):
        super().__init__()
        self.on_click = on_click
        self.width = width
        self.height = height
        self.content = content

    def build(self):
        return Container(
            width=self.width,
            height=self.height,
            on_click=self.on_click,
            gradient=LinearGradient(
                begin=alignment.center_left,
                end=alignment.center_right,
                colors=[
                    colors.ORANGE,
                    colors.RED,
                ],
            ),
            border_radius=100.0,
            content=self.content,
            alignment=alignment.center,
        )
