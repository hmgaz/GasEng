# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_GasEng.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_GasEng(object):
    def setupUi(self, GasEng):
        GasEng.setObjectName("GasEng")
        GasEng.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(GasEng)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(GasEng)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), GasEng.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), GasEng.reject)
        QtCore.QMetaObject.connectSlotsByName(GasEng)

    def retranslateUi(self, GasEng):
        GasEng.setWindowTitle(QtGui.QApplication.translate("GasEng", "GasEng", None, QtGui.QApplication.UnicodeUTF8))
