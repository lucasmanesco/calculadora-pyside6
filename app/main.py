import sys

from calculator import ButtonsGrid, Display, MainWindow, Memo, setupTheme
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':

    # Fix Icon Bug (Win11)
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    # Criando App
    app = QApplication(sys.argv)
    window = MainWindow()

    # Configurando Tema
    setupTheme()

    # Memória
    memo = Memo('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(memo)

    # Display
    display = Display()
    display.setPlaceholderText('Calculate...')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Ajustes
    window.adjustFixedSize()

    # Executando App
    window.show()
    app.exec()
