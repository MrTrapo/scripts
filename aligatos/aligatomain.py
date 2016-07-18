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
        os.environ["USER"]

        QtCore.QObject.connect(self.ui.acceder, QtCore.SIGNAL('clicked()'), self.conecta)
    def conecta(self):
        pas=self.ui.pasw.text()
        uno="""gnome-terminal --tab --maximize --title=\"aligato01.ollin\" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato01; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato02.ollin\" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato02; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato03.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato03; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato04.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato04; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato05.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato05; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato06.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato06; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato07.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato07; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato08.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato08; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato09.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato09; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato10.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato10; exec /bin/bash -i' \" """.format(pas,pas,pas,pas,pas,pas,pas,pas,pas,pas)


        dos="""gnome-terminal --tab --maximize --title=\"aligato13.ollin\" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato01; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato14.ollin\" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato02; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato15.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato03; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato16.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato04; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato17.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato05; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato18.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato06; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato19.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato07; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato20.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato08; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato21.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato09; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato22.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato09; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato23.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato09; exec /bin/bash -i' \" \\
        --tab --maximize --title=\"aligato24.ollin" -e \"/bin/bash -c '/nfs/benito1/Project/common/dev_debug/farm_utils/template.sh $USER $(printf ''%q'' ${}) aligato10; exec /bin/bash -i' \" """.format(pas,pas,pas,pas,pas,pas,pas,pas,pas,pas,pas,pas)

        os.system(uno)
        os.system(dos)

app = QApplication(sys.argv)
aligatos = aligatos()
aligatos.show()
#mainloop q mantiene la  aplicacion
sys.exit(app.exec_())