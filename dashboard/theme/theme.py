from flet import (
    Text,
    FontWeight
)


class Theme:
    def __init__(self):
        """Contiene todo la configuracion del tema de la aplicacion
        """
        super().__init__()

    # region [Colors]
    bg_color = "#252836"
    bg_menu_color = "#1F1D2B"
    principal_text_color = "#FFFFFF"
    disabled_text_color = "#99999F"
    yellow_color = "#FFAB30"
    container_color = "#2D303E"
    # endregion [Colors]

    @staticmethod
    def title_text(value: str, size: int = 20):
        """Crea un texto con el estilo de titulo

        Args:
            value (str): Texto a mostrar
            size (int, optional): Tamaño de la fuente. Por defecto tiene un valor de 20.

        Returns:
            (flet.Text): Texto con el estilo de titulo
        """
        return Text(
            value=value,
            weight=FontWeight.W_600,
            color=Theme.principal_text_color,
            size=size,
        )

    @staticmethod
    def normal_text(value: str, size: int = 15, text_bold: bool = False):
        """Crea un texto con el estilo normal

        Args:
            value (str): Texto a mostrar
            size (int, optional): Tamaño de la fuente. Por defecto tiene un valor de 15.
            text_bold (bool, optional): Indica si el texto es negrita. Por defecto tiene un valor de False.

        Returns:
            (flet.Text): Texto con el estilo normal
        """
        return Text(
            value=value,
            weight=FontWeight.W_600 if text_bold else FontWeight.W_400,
            color=Theme.principal_text_color,
            size=size,
        )

    @staticmethod
    def subtitle_text(value: str, size: int = 15):
        """Crea un texto con el estilo de subtitulo

        Args:
            value (str): Texto a mostrar
            size (int, optional): Tamaño de la fuente. Por defecto tiene un valor de 15.

        Returns:
            (flet.Text): Texto con el estilo de subtitulo
        """
        return Text(
            value=value,
            weight=FontWeight.W_400,
            color=Theme.disabled_text_color,
            size=size,
        )

    @staticmethod
    def small_text(value: str, size: int = 12):
        """Crea un texto con el estilo de pequeño

        Args:
            value (str): Texto a mostrar
            size (int, optional): Tamaño de la fuente. Por defecto tiene un valor de 12.

        Returns:
            (flet.Text): Texto con el estilo de pequeño
        """
        return Text(
            value=value,
            weight=FontWeight.W_400,
            color=Theme.disabled_text_color,
            size=size,
        )
