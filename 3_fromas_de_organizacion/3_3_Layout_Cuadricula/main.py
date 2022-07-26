from PySide6.QtWidgets import QApplication,QMainWindow,QLabel,QGridLayout,QWidget
import sys

class Caja(QLabel):
    def __init__(self,color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        cuadricula=QGridLayout()
        
        cuadricula.addWidget(Caja("red"), 0, 0)
        cuadricula.addWidget(Caja("blue"), 0, 1)
        cuadricula.addWidget(Caja("blue"), 1, 0)
        cuadricula.addWidget(Caja("red"), 1, 1)
        
        widget=QWidget()
        widget.setLayout(cuadricula)
        self.setCentralWidget(widget)
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())
    
    
    # Creacion de cuadricula random
    
#     import random

# # bucles for para generar una cuadrícula
# for fila in range(5):
#     for columna in range(5):
#         # añadimos una caja de color aleatorio
#         color = str(hex(random.randint(0, 16777215)))  # int(0xFFFFFF)
#         cuadricula.addWidget(Caja(f"#{color[2:]}"), fila, columna)
        