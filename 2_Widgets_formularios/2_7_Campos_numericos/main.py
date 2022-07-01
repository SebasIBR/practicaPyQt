from PySide6.QtWidgets import QApplication,QMainWindow,QSpinBox
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        numero=QSpinBox()
        self.setCentralWidget(numero)
        
        numero.setMinimum(0)
        numero.setMaximum(10)
        numero.setRange(0, 10)
        numero.setSingleStep(1)
        
        numero.valueChanged.connect(self.valor_cambiado)
    def valor_cambiado(self,numero):
        print("valor cambiado", numero)
        
        
if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
        