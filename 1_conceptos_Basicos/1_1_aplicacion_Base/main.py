#                 PROGRAMA DE PRUEBA Y APRENDIZAJE DEL USO DE QT Y QTDESGINER 

#                            ---Importacion de librerias--- 

#                       --Importacion de la ventana de aplicacion--

#QApplication: Es el núcleo de un programa en Qt, se requiere para manejar el bucle de la aplicación, 

#encargado de gestionar todas las interacciones con la interfaz gráfica de usuario.

from PySide6.QtWidgets import QApplication


#--                             Importacion de Widget vacio

# Una aplicación requiere por lo menos un widget para mostrar algo en pantalla. Todos los widgets que heredan 

# de QWidget se pueden visualizar como ventanas en sí mismos:

from PySide6.QtWidgets import QWidget 

import sys #Importacion de ------


#Creacion de aplicacion para la interfaz

#-Esta fucncion sin un widget no muestra nada 

app= QApplication(sys.argv)


#Creacion de widget para generar la ventana

window= QWidget()


# mostramos la ventana que se encuentra odulta por defecto

#-muestra la ventana pero se cierra automaticamente

window.show()


# bucle del programa para que la ventan no se cierre 

sys.exit(app.exec_())