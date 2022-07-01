# Aplicacion para lista despegable
from PySide6.QtWidgets import QApplication,QMainWindow,QComboBox
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        lista= QComboBox()
        lista.addItems(["opcion1","opcion2","opcion3"])
        self.setCentralWidget(lista)
        
        
if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())