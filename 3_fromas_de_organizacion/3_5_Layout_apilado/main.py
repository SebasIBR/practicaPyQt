from PySide6.QtWidgets import QApplication,QMainWindow,QLabel,QStackedLayout,QWidget
import sys

from PySide6.QtCore import Qt


class Caja(QLabel):
    def __init__(self,color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout=QStackedLayout()
        
        # Añadimos varios widgets unos sobre otros
        layout.addWidget(Caja("orange"))
        layout.addWidget(Caja("magenta"))
        layout.addWidget(Caja("purple"))
        layout.addWidget(Caja("red"))
        
        widget=QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        self.layout=layout
        
    def keyPressEvent(self, event):
        # detectamos la flecha presionada
        if event.key() == Qt.Key_Right:
            print("Flecha derecha presionada")
        elif event.key() == Qt.Key_Left:
            print("Flecha izquierda presionada")
        # continuamos con el evento por defecto
        event.accept()
    def keyPressEvent(self, event):
        # recuperamos el índice
        indice = self.layout.currentIndex()
        # buscamos el indice máximo del layout contando cuantos widgets tiene
        indice_maximo = self.layout.count() - 1

        # dependiendo de la flecha presionada sumamos o restamos
        if event.key() == Qt.Key_Right:
            indice += 1
        elif event.key() == Qt.Key_Left:
            indice -= 1

        # rectificamos el índice para generar el efecto infinito
        if indice > indice_maximo:
            indice = 0
        if indice < 0:
            indice = indice_maximo

        # finalmente establecemos el nuevo índice
        self.layout.setCurrentIndex(indice)

        # continuamos con el evento por defecto
        event.accept()
    
        
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        