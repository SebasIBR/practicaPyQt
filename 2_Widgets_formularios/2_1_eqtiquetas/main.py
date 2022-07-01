from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QPixmap
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))

        # widget etiqueta
        etiqueta = QLabel("Soy una etiqueta")
        # establecemos el widget central
        self.setCentralWidget(etiqueta)
        
        # Aplica fuente 1 o fuente 2
        # recuperamos la fuente por defecto
        fuente = etiqueta.font()
        # establecemos un tamaño
        fuente.setPointSize(24)
        # la asignamos a la etiqueta
        
        # fuente 2
        
        # cargamos una fuente del sistema
        fuente2 = QFont("Comic Sans MS", 24)
        # la asignamos a la etiqueta
        etiqueta.setFont(fuente)
        imagen=QPixmap("jh.png")
        etiqueta.setPixmap(imagen)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
