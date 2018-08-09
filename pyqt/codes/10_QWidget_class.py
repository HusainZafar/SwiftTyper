import sys
from PyQt5.QtWidgets import QApplication, QWidget

class GUI(QWidget):					#inherit from QWidget
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('PyQt Demo')
		self.resize(300,200)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = GUI()
	gui.show()
	sys.exit(app.exec_())
