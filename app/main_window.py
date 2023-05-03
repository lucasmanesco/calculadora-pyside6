from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from variables import WINDOW_ICON_PATH


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
        icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(icon)

    # Ajustar tamanho fixo da Window
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adicionar Widgets no Layout
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
