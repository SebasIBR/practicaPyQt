# Aplicacion basica de la creacion de un contenedor


from PySide6.QtWidgets import QApplication,QLabel,QMainWindow
import sys

class caja(QLabel):
    def __init__(self,color):
        super().__init__()
        self.styleSheet(f"background-color:{color}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())