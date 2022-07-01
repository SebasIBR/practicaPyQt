import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenidos")
        check=QCheckBox("Acepta terminos y condiciones")
        self.setCentralWidget(check)
        
        check.stateChanged.connect(self.estado_cambiado)
        check.setCheckState(Qt.PartiallyChecked)
    def estado_cambiado(self,estado):
        if estado == Qt.Checked:
            print("Casilla marcada")
        if estado == Qt.Unchecked:
            print("Casilla desmarcada")
        if estado == Qt.PartiallyChecked:
            print("Casilla neutra")
            
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())