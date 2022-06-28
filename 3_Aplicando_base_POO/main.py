# Aplicacion de las lecciones anteriores 

import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton


# Creamos la clase de ventana heredando el QmainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        button=QPushButton("Bienvenido")
        self.setCentralWidget(button)
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())    