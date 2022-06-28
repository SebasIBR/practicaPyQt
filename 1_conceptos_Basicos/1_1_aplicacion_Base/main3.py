# Importacion del bucle
import sys

# Importacion de la libreria que trae la aplicacion la ventana y el boton 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Seteo de app en la aplicacion general
app= QApplication(sys.argv)

# Seteo de la ventana en la variable window
window= QMainWindow()
# Titulo principal de la aplicacion
window.setWindowTitle("Hola Mundo")

# Seteo del boton en un variable y con su respectivo tirulo
button= QPushButton("Bienvenido")

# Centralizacion del boton en la ventana principal
window.setCentralWidget(button)

# Vizualizacion de la ventana
window.show()

# cierre del bucle
sys.exit(app.exec_())

