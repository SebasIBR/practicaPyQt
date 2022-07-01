from PySide6.QtWidgets import QApplication,QMainWindow,QListWidget
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        lista= QListWidget()
        self.setCentralWidget(lista)
        
        lista.addItems(["op1","op2","op3"])
        
        lista.currentItemChanged.connect(self.item_cambiado)
        print(lista.currentItem())
    def item_cambiado(sefl, item):
        print("nuebo item",item.text())
     

if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())