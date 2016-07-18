
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aligatoqt.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(383, 118)
        self.acceder = QtGui.QPushButton(Dialog)
        self.acceder.setGeometry(QtCore.QRect(260, 50, 75, 23))
        self.acceder.setObjectName(_fromUtf8("acceder"))
        self.error = QtGui.QLabel(Dialog)
        self.error.setGeometry(QtCore.QRect(130, 110, 47, 13))
        self.error.setText(_fromUtf8(""))
        self.error.setObjectName(_fromUtf8("error"))
        self.splitter_3 = QtGui.QSplitter(Dialog)
        self.splitter_3.setGeometry(QtCore.QRect(30, 30, 180, 41))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.usu = QtGui.QLabel(self.splitter)
        self.usu.setText(_fromUtf8(""))
        self.usu.setObjectName(_fromUtf8("usu"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_2 = QtGui.QLabel(self.splitter_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pasw = QtGui.QLineEdit(self.splitter_2)
        self.pasw.setObjectName(_fromUtf8("pasw"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.acceder.setText(_translate("Dialog", "ACCEDER", None))
        self.label.setText(_translate("Dialog", "USUARIO:", None))
        self.label_2.setText(_translate("Dialog", "PASSWORD:", None))




