#                 PROGRAMA DE PRUEBA Y APRENDIZAJE DEL USO DE QT Y QTDESGINER 
#                            ---Importacion de librerias--- 
# Generacion de archivo de boton en toda la ventana pero no es funcional 

import sys
from PySide6.QtWidgets import QApplication,QPushButton
app= QApplication(sys.argv)
window= QPushButton("Hola Mundo")
window.show()
sys.exit(app.exec_())