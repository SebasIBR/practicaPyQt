from PySide6.QtWidgets import QApplication,QMainWindow,QDoubleSpinBox
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        numero=QDoubleSpinBox()
        self.setCentralWidget(numero)
        
        numero.setMinimum(0)
        numero.setMaximum(10)
        numero.setRange(0, 10)
        numero.setSingleStep(0.5)
        
        numero.setValue(3.14)
        
        numero.valueChanged.connect(self.valor_cambiado)
        print(numero.value())
    def valor_cambiado(self,numero):
        print("valor cambiado", numero)
        
        
if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())