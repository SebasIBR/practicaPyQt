# Importacion del bucle
import sys

# Importacion de la aplicacion y de gestor de ventanas
from PySide6.QtWidgets import QApplication, QMainWindow

# Importacion y almacenamiento de la aplicacion
app=QApplication(sys.argv)

# Titulo de la ventana principal
window=QMainWindow()
window.setWindowTitle("Hola mundo")

window.show()

sys.exit(app.exec_())