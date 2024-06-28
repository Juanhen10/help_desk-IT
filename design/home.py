import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from login_ui import Ui_MainWindow  # Altere para o nome do seu arquivo de interface gerado

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
