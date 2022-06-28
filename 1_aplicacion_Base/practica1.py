import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton

app=QApplication(sys.argv)
window=QMainWindow()
window.setWindowTitle("Hola Mndo")

button=QPushButton("Bienvenido")

window.setCentralWidget(button)

window.show()

sys.exit(app.exec_())