import sys
from PyQt5 import QtCore, QtWidgets


class Ejemplo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.marcas = {"Alfa Romeo": ["MiTo", "Giulietta", "4C"], 
                       "Aston Martin": ["DB9", "Rapide", "Vanquish"],
                       "Audi": ["A1", "A3", "A4"]
                      }
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Comboxs enlazados')
        self.setGeometry(0,  0, 600, 400)
        layout = QtWidgets.QGridLayout(self)
        layout.setAlignment(QtCore.Qt.AlignTop)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(0, 0)
        lb_mar = QtWidgets.QLabel(self, text = "Marca")
        lb_mod = QtWidgets.QLabel(self, text = "Modelo")
        self.combo_mar = QtWidgets.QComboBox(self)
        self.combo_mod = QtWidgets.QComboBox(self)
        layout.addWidget(lb_mar, 0, 0, QtCore.Qt.AlignCenter)
        layout.addWidget(lb_mod, 0, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.combo_mar, 1, 0)
        layout.addWidget(self.combo_mod, 1, 1)
        self.setLayout(layout)
        self.combo_mar.currentIndexChanged[str].connect(self.llenar_comboBox_modelos)
        self.llenar_comboBox_marcas()
        self.show()   

    @QtCore.pyqtSlot()      
    def llenar_comboBox_marcas(self):
        self.combo_mar.clear()
        self.combo_mar.addItems(sorted(self.marcas.keys()))

    @QtCore.pyqtSlot(str)    
    def llenar_comboBox_modelos(self,  marca):
        self.combo_mod.clear()
        self.combo_mod.addItems(self.marcas[marca])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ejemplo()
    sys.exit(app.exec_())