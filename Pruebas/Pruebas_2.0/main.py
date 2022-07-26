from ui.ui import *
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6 import QtCore
from PySide6.QtCore import Qt
import sys
from database import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widgets= Ui_MainWindow()
        self.widgets.setupUi(self)
        
        self.widgets.lista_departamentos.addItems(departamentos)
        self.widgets.lista_departamentos.setCurrentText(defecto_departamento)
        # self.widgets.lista_municipios.setCurrentText(defecto_municipio)
        # self.widgets.lista_departamentos.setPlaceholderText(defecto_departamento)
        # self.widgets.lista_departamentos.setCurrentIndex(-1)
        self.widgets.lista_municipios.setPlaceholderText(defecto_municipio)
        self.widgets.lista_municipios.setCurrentIndex(-1)
        self.widgets.color.addItems(colores)
        self.widgets.color.setCurrentText(defecto_color)
        self.widgets.aceptar.clicked.connect(self.aceptar) 
        
        self.indice=self.widgets.lista_departamentos.currentIndexChanged.connect(self.municipo)
        
    def keyPressEvent(self,event):
        if event.key() == QtCore.Qt.Key_Return:
            print("pressed")
        event.accept()
    
    def municipo(self,indice):
        muni=[]
        index=indice+1
        for i in database:
            if index==i[2]:
                muni.append(i[1])
        self.widgets.lista_municipios.clear()
        self.widgets.lista_municipios.addItems(muni)
        # self.widgets.lista_municipios.setCurrentText(defecto_municipio)
        self.widgets.lista_municipios.setPlaceholderText("")
                
        
    def aceptar(self):
        self.estado=True
        self.lista=self.widgets.lista_departamentos.currentText()
        self.lista2=self.widgets.lista_municipios.currentText()
        self.lista3=self.widgets.color.currentText()
        print(self.estado)
        if self.widgets.lista_municipios.currentIndex()==-1:
            self.estado=False
            print(self.estado)
        Guardar(self.lista,self.lista2,self.lista3,self.estado)
        
if __name__== "__main__":
    app=QApplication()
    
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
    