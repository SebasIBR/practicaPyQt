from ui.ui import *
from PySide6.QtWidgets import QApplication,QMainWindow
import sys
from database import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widgets= Ui_MainWindow()
        self.widgets.setupUi(self)
        
        self.widgets.lista_departamentos.addItems(departamentos)
        self.widgets.lista_departamentos.setPlaceholderText(defecto_departamento)
        self.widgets.lista_departamentos.setCurrentIndex(-1)
        self.widgets.lista_municipios.setPlaceholderText(defecto_municipio)
        self.widgets.lista_municipios.setCurrentIndex(-1)
        self.widgets.aceptar.clicked.connect(self.aceptar) 
        
        self.indice=self.widgets.lista_departamentos.currentIndexChanged.connect(self.municipo)
    
    def municipo(self,indice):
        muni=[]
        index=indice+1
        for i in database:
            if index==i[2]:
                muni.append(i[1])
        self.widgets.lista_municipios.clear()
        self.widgets.lista_municipios.addItems(muni)
        self.widgets.lista_municipios.setPlaceholderText("")
                
        
    def aceptar(self):
        self.lista=self.widgets.lista_departamentos.currentText()
        self.lista2=self.widgets.lista_municipios.currentText()
        Guardar(self.lista,self.lista2)
        print(self.lista,self.lista2)

if __name__== "__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
    