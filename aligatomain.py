from __future__ import division
import os
from PyQt4.QtGui import *
from aligatoqt import *
#libreria  q contiene  los  widgets importando todo * lo de QtGui
import sys
class aligatos(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("ALIGATOS")
        os.system("USER=$(whoami)")
        self.ui.usu.setText(os.environ["USER"])
        self.ui.pasw.setEchoMode(QtGui.QLineEdit.Password)
        QtCore.QObject.connect(self.ui.acceder, QtCore.SIGNAL('clicked()'), self.conecta)
    def conecta(self):
        user = self.ui.usu.text()
        passwd = self.ui.pasw.text()
        command = 'htop'
        root = 'gnome-terminal '
        aligatos1_10 = [
        'aligato01.ollin',
        'aligato02.ollin',
        'aligato03.ollin',
        'aligato04.ollin',
        'aligato05.ollin',
        'aligato06.ollin',
        'aligato07.ollin',
        'aligato08.ollin',
        'aligato09.ollin',
        'aligato10.ollin'
        ]
        aligatos1 = [
        'aligato13.ollin',
        'aligato14.ollin',
        'aligato15.ollin',
        'aligato16.ollin',
        'aligato17.ollin',
        'aligato18.ollin',
        'aligato19.ollin',
        'aligato20.ollin',
        'aligato21.ollin',
        'aligato22.ollin',
        'aligato23.ollin',
        'aligato24.ollin'
        ]
        for i in aligatos1_10:
            temp = '--tab -t "{0}" -e "sshpass -p "{1}" ssh -t {2} -l {3} -o StrictHostKeyChecking=no "{4}"" '.format(i.split('.')[0], passwd, i, user, command)
            root += temp
        os.system(root)
        root='gnome-terminal '
        for i in aligatos1:
            temp = '--tab -t "{0}" -e "sshpass -p "{1}" ssh -t {2} -l {3} -o StrictHostKeyChecking=no "{4}"" '.format(i.split('.')[0], passwd, i, user, command)
            root += temp
        os.system(root)
#os.system(dos)
        self.close()
app = QApplication(sys.argv)
aligatos = aligatos()
aligatos.show()
#mainloop q mantiene la  aplicacion
sys.exit(app.exec_())