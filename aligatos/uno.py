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
        pas=self.ui.pasw.text()
        uno="""gnome-terminal --tab --title=\"aligato01.ollin\" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato01; exec /bin/bash -i' \" \\
        --tab --title=\"aligato02.ollin\" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato02; exec /bin/bash -i' \" \\
        --tab --title=\"aligato03.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato03; exec /bin/bash -i' \" \\
        --tab --title=\"aligato04.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato04; exec /bin/bash -i' \" \\
        --tab --title=\"aligato05.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato05; exec /bin/bash -i' \" \\
        --tab --title=\"aligato06.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato06; exec /bin/bash -i' \" \\
        --tab --title=\"aligato07.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato07; exec /bin/bash -i' \" \\
        --tab --title=\"aligato08.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato08; exec /bin/bash -i' \" \\
        --tab --title=\"aligato09.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato09; exec /bin/bash -i' \" \\
        --tab --title=\"aligato10.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato10; exec /bin/bash -i' \" """.format(pas)


        dos="""gnome-terminal --tab --title=\"aligato13.ollin\" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato01; exec /bin/bash -i' \" \\
        --tab --title=\"aligato14.ollin\" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato02; exec /bin/bash -i' \" \\
        --tab --title=\"aligato15.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato03; exec /bin/bash -i' \" \\
        --tab --title=\"aligato16.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato04; exec /bin/bash -i' \" \\
        --tab --title=\"aligato17.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato05; exec /bin/bash -i' \" \\
        --tab --title=\"aligato18.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato06; exec /bin/bash -i' \" \\
        --tab --title=\"aligato19.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato07; exec /bin/bash -i' \" \\
        --tab --title=\"aligato20.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato08; exec /bin/bash -i' \" \\
        --tab --title=\"aligato21.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato09; exec /bin/bash -i' \" \\
        --tab --title=\"aligato22.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato09; exec /bin/bash -i' \" \\
        --tab --title=\"aligato23.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato09; exec /bin/bash -i' \" \\
        --tab --title=\"aligato24.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${0}) aligato10; exec /bin/bash -i' \" """.format(pas)

        os.system(uno)
        os.system(dos)
	self.close()
app = QApplication(sys.argv)
aligatos = aligatos()
aligatos.show()
#mainloop q mantiene la  aplicacion
sys.exit(app.exec_())
