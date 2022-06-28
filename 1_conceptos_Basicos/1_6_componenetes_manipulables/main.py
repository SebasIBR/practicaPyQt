# Aplicacion en la cual podemos cambiar el estado y valor de un boton 
import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenidos a mi app")
        self.resize(360,360)
        
        button=QPushButton("Soy un boton")
        self.setCentralWidget(button)
        
        button.setCheckable(True)
        button.clicked.connect(self.boton_alternador)
        
        self.button =button
        
        
    def boton_alternador(self,valor):
        if valor:
            self.button.setText("Activado")
        else:
            self.button.setText("Desactivado")
            
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())