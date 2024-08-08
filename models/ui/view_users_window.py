# view_users_window.py

import sys
import requests
from PySide6.QtCore import QRect, QMetaObject, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class ViewUsersWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Usuários")
        self.setGeometry(100, 100, 600, 400)
        self.setup_ui()

    def setup_ui(self):
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.layout = QVBoxLayout(self.centralwidget)

        self.table = QTableWidget(self.centralwidget)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Nome", "Email", "Departamento", "PIN", "Administrador"])

        self.layout.addWidget(self.table)

        self.load_button = QPushButton("Carregar Usuários", self.centralwidget)
        self.load_button.clicked.connect(self.load_users)
        self.layout.addWidget(self.load_button)

        self.load_users()

    def load_users(self):
        try:
            response = requests.get('http://localhost:5000/users')
            if response.status_code == 200:
                users = response.json()
                self.table.setRowCount(len(users))
                for row, user in enumerate(users):
                    self.table.setItem(row, 0, QTableWidgetItem(user['nome']))
                    self.table.setItem(row, 1, QTableWidgetItem(user['email']))
                    self.table.setItem(row, 2, QTableWidgetItem(user['departamento']))
                    self.table.setItem(row, 3, QTableWidgetItem(user['pin']))
                    self.table.setItem(row, 4, QTableWidgetItem("Sim" if user['is_admin'] else "Não"))
            else:
                print(f"Erro ao carregar usuários: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ViewUsersWindow()
    window.show()
    sys.exit(app.exec())
