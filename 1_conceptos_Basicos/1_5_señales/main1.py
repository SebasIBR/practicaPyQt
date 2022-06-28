# En esta aplicacion le crearemos la funcionalidad al boton 

# Crearemos slots que nos indican las funciones y conecciones de los botones y eventos 

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botonon")
        button=QPushButton("Presioname")
        self.setCentralWidget(button)
        self.resize(480,360)
        
        button.pressed.connect(self.boton_pulsado)
        button.released.connect(self.boton_liberado)
        
    def boton_pulsado(self):
        print("Me has pulsado")
    
    def boton_liberado(self):
        print("Me has librado")

if __name__=="__main__":
    app=QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())