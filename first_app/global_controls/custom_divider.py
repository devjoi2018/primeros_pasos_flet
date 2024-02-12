from flet import (
    Container,
    UserControl,
)


class CustomDivider(UserControl):
    def __init__(self, color, height=1.0, width=100.0):
        super().__init__()
        self.color = color
        self.height = height
        self.width = width

    def build(self):
        return Container(
            border_radius=100.0,
            width=self.width,
            height=self.height,
            bgcolor=self.color,
        )
