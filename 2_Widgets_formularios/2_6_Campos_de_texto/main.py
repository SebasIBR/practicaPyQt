from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        texto=QLineEdit()
        self.setCentralWidget(texto)
        
        texto.setMaxLength(10)
        texto.setPlaceholderText("escribe maximo 10 caracteres")
        
        texto.textChanged.connect(self.texto_cambiado)
        texto.returnPressed.connect(self.enter_presionado)
        
    def texto_cambiado(self, texto):
        print("texto cambiado",texto)
        
    def enter_presionado(self):
        texto=self.centralWidget().text()
        print("enter presionado, texto",texto)
        
if __name__=="__main__":
    app= QApplication()
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())
        