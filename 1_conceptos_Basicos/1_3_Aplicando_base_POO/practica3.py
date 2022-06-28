import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo Carnico")
        button=QPushButton("Bienvenidos a SGC")
        self.setCentralWidget(button)
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())