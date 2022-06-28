# En este archivo implementaremos el tamaño de las ventanas
# se toma el ancho y el largo del tamaño en pixeles y se establece como un tamaño minimo de la aplicion

import sys 
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
from PySide6.QtCore import QSize #Importacion de la libreria para cambiar el tamaño

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo Carnico")
        button= QPushButton("Bienvenidos a SGC")
        self.setCentralWidget(button)
        
        self.resize(480,340)
        # self.setMinimumSize(QSize(480,320))
        # self.setMaximumSize(QSize(480,320))
        # self.setFixedSize(QSize(480,320))
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())