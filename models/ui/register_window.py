# register_window.py

import base64
import sys
import requests
from PySide6.QtCore import QCoreApplication, QRect, QMetaObject
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QLabel, QToolButton, QPushButton, QLineEdit, QStatusBar, QCheckBox, QMessageBox, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon, QIntValidator, QPixmap 
import webbrowser
from view_users_window import ViewUsersWindow  # Importando a janela de visualização de usuários
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent
from PySide6.QtCore import Qt, QMimeData

class DraggableImageLabel(QLabel):
    def __init__(self, parent=None):
        super(DraggableImageLabel, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls and urls[0].isLocalFile():
            file_path = urls[0].toLocalFile()
            self.setPixmap(QPixmap(file_path).scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio))
            self.image_path = file_path  # Armazena o caminho da imagem

    def clear_image(self):
        self.setPixmap(QPixmap())
        self.image_path = ""


   
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(486, 430)
        # deixando trasparente
        MainWindow.setWindowOpacity(0.9)  # Ajuste a opacidade conforme necessário
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Fundo transparente
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove a borda da janela
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 40, 341, 500))
        self.frame.setStyleSheet(u"background-color: #49494A;\n"
                                 "border-radius: 15px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.adm_painel = QFrame(self.frame)
        self.adm_painel.setObjectName(u"adm_painel")
        self.adm_painel.setGeometry(QRect(10, 10, 321, 41))
        self.adm_painel.setStyleSheet(u"QFrame{\n"
                                      "border-radius: 15px;\n"
                                      "background-color: #FFFFFF;\n"
                                      "}")
        self.adm_painel.setFrameShape(QFrame.Shape.StyledPanel)
        self.adm_painel.setFrameShadow(QFrame.Shadow.Raised)
        self.titulo_txt = QLabel(self.adm_painel)
        self.titulo_txt.setObjectName(u"titulo_txt")
        self.titulo_txt.setGeometry(QRect(25, 0, 271, 41))
        self.titulo_txt.setStyleSheet(u"color: #49494A;")
        # botão de fechar o app
        self.close_btn = QToolButton(self.adm_painel)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(280, 10, 22, 22))
        self.close_btn.setIcon(QIcon("design/icons/fechar.png"))
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.close_btn.setEnabled(True)
        self.close_btn.setStyleSheet(u"QToolButton{\n"
                                    "border-radius: 15px;\n"
                                    "background-color: #FFFFFF;\n"
                                    "}")
        # home 

        self.adm_home = QFrame(self.frame)
        self.adm_home.setObjectName(u"adm_home")
        self.adm_home.setGeometry(QRect(10, 60, 321, 300))
        self.adm_home.setStyleSheet(u"QFrame{\n"
                                    "border-radius: 15px;\n"
                                    "background-color: #FFFFFF;\n"
                                    "}")
        self.adm_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.adm_home.setFrameShadow(QFrame.Shadow.Raised)
        # botão de confirmar registro
        self.registro_btn = QPushButton(self.adm_home)
        self.registro_btn.setObjectName(u"registro_btn")
        self.registro_btn.setEnabled(True)
        self.registro_btn.setGeometry(QRect(160, 250, 91, 31))
        self.registro_btn.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.registro_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.registro_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        font = QFont()
        font.setBold(False)
        self.registro_btn.setStyleSheet("QPushButton {"
                                  "    background-color: rgb(27, 27, 27);"  # Cor de fundo do botão
                                  "    color: white;"  # Cor do texto
                                  "    border-radius: 5px;"
                                  "    min-width: 100px;"  # Definindo largura mínima
                                  "    max-width: 150px;"  # Definindo largura máxima
                                  "    height: 20px"
                                  "}"
                                  "QPushButton:hover {"
                                  "    background-color: rgba(0, 217, 113, 1);"
                                  "}"
                                  "QPushButton:pressed {"
                                  "    background-color: rgba(0, 217, 113, 0.5);"
                                  "}")
        # botão de cancelamento.
        self.cancel_btn = QPushButton(self.adm_home)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(40, 250, 91, 31))
        self.cancel_btn.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.cancel_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.cancel_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.cancel_btn.setStyleSheet("QPushButton {"
                                  "    background-color: rgb(27, 27, 27);"  # Cor de fundo do botão
                                  "    color: white;"  # Cor do texto
                                  "    border-radius: 5px;"
                                  "    min-width: 100px;"  # Definindo largura mínima
                                  "    max-width: 150px;"  # Definindo largura máxima
                                  "    height: 20px"
                                  "}"
                                  "QPushButton:hover {"
                                  "    background-color: rgba(0, 217, 113, 1);"
                                  "}"
                                  "QPushButton:pressed {"
                                  "    background-color: rgba(0, 217, 113, 0.5);"
                                  "}")
        # NOME
        self.nome_txt = QLabel(self.adm_home)
        self.nome_txt.setObjectName(u"nome_txt")
        self.nome_txt.setGeometry(QRect(25, 10, 49, 16))
        self.nome_txt.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.nome_line = QLineEdit(self.adm_home)
        self.nome_line.setObjectName(u"nome_line")
        self.nome_line.setGeometry(QRect(30, 25, 241, 30))
        self.nome_line.setStyleSheet(u"QLineEdit {"
                                    "       border-radius: 5px;"
                                    "       height: 15px;"
                                    "       min-width: 250px;"  # Definindo largura mínima
                                    "       max-width: 200px;"  # Definindo largura máxima
                                    "       text-align: center"
                                    "}")
        
        # EMAIL #
        self.email_txt = QLabel(self.adm_home)
        self.email_txt.setObjectName(u"email_txt")
        self.email_txt.setGeometry(QRect(25, 55, 41, 20))
        self.email_txt.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.email_line = QLineEdit(self.adm_home)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(30, 74, 241, 30))
        self.email_line.setStyleSheet(u"QLineEdit {"
                                    "       border-radius: 5px;"
                                    "       height: 15px;"
                                    "       min-width: 250px;"  # Definindo largura mínima
                                    "       max-width: 200px;"  # Definindo largura máxima
                                    "       text-align: center"
                                    "}")
                    
        # DEPARTAMENTO 
        self.departamento_txt = QLabel(self.adm_home)
        self.departamento_txt.setObjectName(u"departamento_txt")
        self.departamento_txt.setGeometry(QRect(25, 105, 100, 25))
        self.departamento_txt.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_4 = QLineEdit(self.adm_home)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 125, 241, 30))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {"
                                    "       border-radius: 5px;"
                                    "       height: 15px;"
                                    "       min-width: 250px;"  # Definindo largura mínima
                                    "       max-width: 200px;"  # Definindo largura máxima
                                    "       text-align: center"
                                    "}")
        # configuração do PIN para validar apenas números
        self.pin_txt = QLabel(self.adm_home)
        self.pin_txt.setObjectName(u"pin_txt")
        self.pin_txt.setGeometry(QRect(25, 160, 31, 20))
        self.pin_txt.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.pin_line = QLineEdit(self.adm_home)
        self.pin_line.setObjectName(u"pin_line")
        self.pin_line.setGeometry(QRect(55, 160, 41, 22))
        self.pin_line.setStyleSheet(u"QLineEdit {"
                                    "       border-radius: 5px;"
                                    "       height: 15px;"
                                    "       min-width: 100px;"  # Definindo largura mínima
                                    "       max-width: 50px;"  # Definindo largura máxima
                                    "       text-align: center"
                                    "}")
         # Adicione um QLabel para exibir a imagem de perfil
        # Dentro da sua classe Ui_MainWindow ou MainWindow

        self.imagem = DraggableImageLabel(self.adm_home)
        self.imagem.setGeometry(QRect(90, 195, 145, 40))
        self.imagem.setStyleSheet("border-radius: 10px; border: 2px dashed #aaa;")
        self.imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imagem.setText("ARRASTE A IMAGEM")

  

        self.adm_txt = QLabel(self.adm_home)
        self.adm_txt.setObjectName(u"adm_txt")
        self.adm_txt.setGeometry(QRect(184, 160, 101, 20))
        self.adm_txt.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.admin_btn = QCheckBox(self.adm_home)
        self.admin_btn.setObjectName(u"admin_btn")
        self.admin_btn.setGeometry(QRect(170, 160, 101, 20))
        self.admin_btn.setStyleSheet(u"QCheckBox {"
                                    "       border-radius: 7px;"
                                    "       height: 15px;"
                                    "       min-width: 15px;"  # Definindo largura mínima
                                    "       max-width: 10px;"  # Definindo largura máxima
                                    "       text-align: center"
                                    
                                    "}")
        self.admin_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        

        # Adicionando botão para abrir a janela de visualização de usuários
        self.view_users_btn = QToolButton(self.adm_home)
        self.view_users_btn.setObjectName(u"view_users_btn")
        self.view_users_btn.setIcon(QIcon("design/icons/lista-de-controle.png"))
        self.view_users_btn.setGeometry(QRect(280, 220, 25, 20))
        self.view_users_btn.setStyleSheet(u"color: rgb(0, 0, 0);"
                                          "background-color: #FFFFFF ")
        self.view_users_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.view_users_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Conectando o botão de visualizar usuários para abrir a janela de visualização
        self.view_users_btn.clicked.connect(self.open_view_users_window)
        self.close_btn.clicked.connect(self.sair)
        self.cancel_btn.clicked.connect(self.cancelar)
        self.registro_btn.clicked.connect(self.registrar_usuario)

        self.imagem.setAcceptDrops(True)
        
        
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo_txt.setText(QCoreApplication.translate("MainWindow", 
                                                           u"<html><head/><body><p align=\"center\"><span style=\"color:#49494A; font-family:'Josefin Sans';\">REGISTRO DE USUARIOS</span></p></body></html>", None))
        self.registro_btn.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.nome_line.setText("")
        self.email_line.setText("")
        self.pin_line.setText("")
        self.lineEdit_4.setText("")
        self.nome_txt.setText(QCoreApplication.translate("MainWindow", 
                                                           u"<html><head/><body><p align=\"center\"><span style=\"color:#49494A; font-family:'Josefin Sans';\">NOME</span></p></body></html>", None))
        self.departamento_txt.setText(QCoreApplication.translate("MainWindow", 
                                                           u"<html><head/><body><p align=\"center\"><span style=\"color:#49494A; font-family:'Josefin Sans';\">DEPARTAMENTO</span></p></body></html>", None))
        self.email_txt.setText(QCoreApplication.translate("MainWindow", 
                                                           u"<html><head/><body><p align=\"center\"><span style=\"color:#49494A; font-family:'Josefin Sans';\">EMAIL</span></p></body></html>", None))
        self.pin_txt.setText(QCoreApplication.translate("MainWindow", 
                                                           u"<html><head/><body><p align=\"center\"><span style=\"color:#49494A; font-family:'Josefin Sans';\">PIN</span></p></body></html>", None))
        self.imagem.setText(QCoreApplication.translate("MainWindow", 
                                                           u"<html><head/><body><p align=\"center\"><span style=\"color:#49494A; font-family:'Josefin Sans';\">ARRASTE A IMAGEM</span></p></body></html>", None))
        #self.perfil_foto.setText(QCoreApplication.translate("MainWindow", u"Foto de Perfil:", None))
        self.admin_btn.setText(QCoreApplication.translate("MainWindow", u"ADM", None))
        self.adm_txt.setText(QCoreApplication.translate("MainWindow", 
                                                           u"<html><head/><body><p align=\"center\"><span style=\"color:#49494A; font-family:;\">ADMINISTRADOR</span></p></body></html>", None))

    def open_view_users_window(self):
        self.view_users_window = ViewUsersWindow()
        self.view_users_window.show()

    def sair(self):
        sys.exit(app.exec())

    def cancelar(self):
        self.nome_line.setText("")
        self.email_line.setText("")
        self.pin_line.setText("")
        self.lineEdit_4.setText("")
        self.admin_btn.setChecked(False)
        self.imagem.clear_image()

    def registrar_usuario(self):
        nome = self.nome_line.text()
        email = self.email_line.text()
        pin = self.pin_line.text()
        departamento = self.lineEdit_4.text()  # Corrigido para pegar o texto correto
        is_admin = self.admin_btn.isChecked()

        if not nome or not email or not pin or not departamento:
            QMessageBox.warning(self.centralwidget, "Erro", "Por favor, preencha todos os campos.")
            return

        # Verifica se uma imagem foi selecionada
        if not self.imagem.image_path:  # Corrigido para pegar o caminho da imagem corretamente
            QMessageBox.warning(self.centralwidget, "Erro", "Por favor, selecione uma imagem.")
            return

        try:
            with open(self.imagem.image_path, 'rb') as f:  # Corrigido para pegar o caminho da imagem corretamente
                imagem_bytes = f.read()

            data = {
                'nome': nome,
                'email': email,
                'pin': pin,
                'departamento': departamento,
                'is_admin': is_admin,
                'imagem': base64.b64encode(imagem_bytes).decode()  # Envia a imagem como base64
            }

            headers = {'Content-Type': 'application/json'}
            response = requests.post('http://localhost:5000/register', json=data, headers=headers)

            if response.status_code == 200:
                QMessageBox.information(self.centralwidget, "Sucesso", "Usuário registrado com sucesso!")
                self.cancelar()  # Limpa os campos após o registro bem-sucedido
            elif response.status_code == 409:
                QMessageBox.warning(self.centralwidget, "Erro", "Email já registrado!")
            else:
                QMessageBox.warning(self.centralwidget, "Erro", f"Erro ao registrar usuário: {response.text}")

        except FileNotFoundError:
            QMessageBox.warning(self.centralwidget, "Erro", "Arquivo da imagem não encontrado.")
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Erro ao enviar dados: {str(e)}")

        def mostrar_mensagem(self, titulo, mensagem):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle(titulo)
            msg.setText(mensagem)
            msg.exec_() 
                            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
