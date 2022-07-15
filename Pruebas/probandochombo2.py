# Aplicacion para lista despegable
from PySide6.QtWidgets import QApplication,QMainWindow,QComboBox,QPushButton
from PySide6.QtCore import QSize, Qt
import sys
from sdf import *
from db import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widgets= Ui_MainWindow()
        self.widgets.setupUi(self)
        self.widgets.lista.addItems(lista_departamentos)
        self.widgets.lista.setPlaceholderText(defecto_departamento)
        self.widgets.lista.setCurrentIndex(-1)
        # Señales
        self.widgets.boton.clicked.connect(self.aceptar)   
    def aceptar(self):
        self.lista=self.widgets.lista.currentText()
        nuevo_departamento(self.lista)
        print(self.lista)
        # self.nuevo=self.widgets.lista.insertItems(0, self.lista)
        
        
        # for letras in self.widgets.lista:
        #     print(letras)
        # self.widgets.texto.setText(self.lista)
        # self.widgets.lista.addItems(self.lista)
 
        
        
        
        
        
        
if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())