# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledOkMvOl.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(602, 365)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 90, 561, 71))
        self.container = QHBoxLayout(self.horizontalLayoutWidget)
        self.container.setObjectName(u"container")
        self.container.setContentsMargins(0, 0, 0, 0)
        self.lista_departamentos = QComboBox(self.horizontalLayoutWidget)
        self.lista_departamentos.setObjectName(u"lista_departamentos")

        self.container.addWidget(self.lista_departamentos)

        self.lista_municipios = QComboBox(self.horizontalLayoutWidget)
        self.lista_municipios.setObjectName(u"lista_municipios")

        self.container.addWidget(self.lista_municipios)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 40, 561, 31))
        self.titulos = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.titulos.setObjectName(u"titulos")
        self.titulos.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.titulos.addWidget(self.label_2)

        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.titulos.addWidget(self.label)

        self.aceptar = QPushButton(self.centralwidget)
        self.aceptar.setObjectName(u"aceptar")
        self.aceptar.setGeometry(QRect(400, 280, 181, 31))
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(50, 190, 511, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.color = QComboBox(self.horizontalLayoutWidget_3)
        self.color.setObjectName(u"color")

        self.horizontalLayout.addWidget(self.color)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 602, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Departamentos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Municipios", None))
        self.aceptar.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
    # retranslateUi

