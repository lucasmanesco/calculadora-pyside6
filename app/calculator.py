import easyfunc as ef
import qdarktheme
import variables as v
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QVBoxLayout, QWidget)


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{v.PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{v.PRIMARY_COLOR}",
            },
        },
        additional_qss=f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {v.PRIMARY_COLOR};}}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {v.DARKER_PRIMARY_COLOR};}}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {v.DARKEST_PRIMARY_COLOR};}}"""
    )


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Estrutura Básica e Settings da Window
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da Window
        self.setWindowTitle('Calculadora')

        # Ícone da Window
        icon = QIcon(str(v.WINDOW_ICON_PATH))
        self.setWindowIcon(icon)

    # Ajustar tamanho fixo da Window
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adicionar Widgets no Layout
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)


class Display(QLineEdit):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(F'font-size: {v.BIG_FONT_SIZE}px;')
        self.setMinimumHeight(v.BIG_FONT_SIZE * 2)
        self.setMinimumWidth(v.MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[v.TEXT_MARGIN for _ in range(4)])


class Memo(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {v.SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(v.MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if ef.isNumOrDot(buttonText) and not ef.isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, i, j)
