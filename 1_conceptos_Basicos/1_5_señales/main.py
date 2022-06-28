# En esta aplicacion le crearemos la funcionalidad al boton 

# Crearemos slots que nos indican las funciones y conecciones de los botones y eventos 

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botonon")
        button=QPushButton("Clickeame")
        self.setCentralWidget(button)
        self.resize(480,360)
        button.clicked.connect(self.boton_clicado)
        
    def boton_clicado(self):
        print("Me has clicado")

        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())