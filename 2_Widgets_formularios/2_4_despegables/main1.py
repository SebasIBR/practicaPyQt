from PySide6.QtWidgets import QApplication,QMainWindow,QComboBox
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        lista=QComboBox()
        self.setCentralWidget(lista)
        lista.addItems([" ","opc1","opc2"])
        # señales
        lista.currentIndexChanged.connect(self.indice_cambiado)
        lista.currentTextChanged.connect(self.texto_cambiado)
    def indice_cambiado(self, indice):
        print("nuevo indice",indice)
    def texto_cambiado(self, texto):
        print("nuevo texto",texto)
        
if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())