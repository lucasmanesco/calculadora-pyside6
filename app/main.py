import sys

from main_window import MainWindow
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
    # Ajustes
    window.adjustFixedSize()
    # Executando App
    window.show()
    app.exec()
