from flet import Page


class LoginController:
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def button_clicked(self, e):
        print("Button clicked")

    def login_button_clicked(self, e):
        print("Login button clicked")
