import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle('PyQt Demo')
win.resize(300,200)

win.show()

sys.exit(app.exec_())
