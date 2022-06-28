# Modificacion del titulo del texto
import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QLineEdit
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenidos")
        self.resize(480,320)
        
        text=QLineEdit()
        self.setCentralWidget(text)
        
        text.textChanged.connect(self.texto_modificado)
        
        self.text=text
        
    def texto_modificado(self):
        texto_recuperado=self.text.text()
        self.setWindowTitle(texto_recuperado)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())