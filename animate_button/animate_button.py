import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    # Varible que controla la animacion de si se muestra o no el contenido
    global reset_animation
    reset_animation = False

    # Funcion que contiene un control de puntos animados.
    def dots():
        dot_design = ft.Container(
            height=4,
            width=4,
            border_radius=100,
            bgcolor=ft.colors.BLACK,
        )
        quantity = 3
        dots = [dot_design for _ in range(quantity)]
        return ft.Row(spacing=2, controls=dots)

    # Funcion que se encarga de animar el contenido
    def animate(e):
        global reset_animation
        button.offset = ft.transform.Offset(
            0, 0) if reset_animation else ft.transform.Offset(0, 1)
        first_text.offset = ft.transform.Offset(
            0, -1) if reset_animation else ft.transform.Offset(0, 0)
        # Se cambia el valor de la variable para que la proxima vez que se llame a la funcion
        reset_animation = not reset_animation
        button.update()
        first_text.update()

    first_text = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Row(
            spacing=4,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value="Processing",
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLACK,
                ),
                dots(),
            ],
        ),
        offset=ft.transform.Offset(0, -1),
        animate_offset=ft.animation.Animation(
            700,
            ft.AnimationCurve.EASE_IN_OUT,
        ),
    )

    # Contenido que se va a animar
    button = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Text(
            value="Pay",
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
        ),
        offset=ft.transform.Offset(0, 0),
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=[
                "#3DACF5",
                "#5698F5",
            ]
        ),
        animate_offset=ft.animation.Animation(
            700,
            ft.AnimationCurve.EASE_OUT,
        ),
    )

    page.add(
        ft.Container(
            width=200,
            height=50,
            bgcolor=ft.colors.WHITE,
            border_radius=100,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(
                color=ft.colors.BLACK38,
                blur_radius=10,
                offset=ft.transform.Offset(0, 3),
            ),
            content=ft.Stack(
                controls=[
                    button,
                    first_text,
                ],
            ),
            on_click=animate,
        ),
    )


ft.app(target=main)
