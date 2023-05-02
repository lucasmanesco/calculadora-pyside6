from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Estrutura Básica da Window
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # Título da Window
        self.setWindowTitle('Calculadora')

    # Ajustando tamanho fixo da Window
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())