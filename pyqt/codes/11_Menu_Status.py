import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon

baseDir = '/home/ubuntub/pyqt/'
imagesDir = baseDir + 'images/'

class GUI(QMainWindow):					#inherit from QMainWindow
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):			
		self.setWindowTitle('PyQt Demo')
		self.resize(300,200)
		self.addMenuAndStatus()

	def addMenuAndStatus(self):
		self.statusBar().showMessage('Hello!')	#QMainWindow: can now use built-in widgets
							#that QWidget doesn't have
		menubar = self.menuBar()

		fileMenu = menubar.addMenu('File')
		newAction = QAction('New',self)
		newAction.setStatusTip('New File')
		exitIcon = QIcon(imagesDir + 'exit.jpg')
		exitAction = QAction(exitIcon,'Exit',self)
		exitAction.triggered.connect(self.close)
		exitAction.setShortcut('Ctrl+Q')
		fileMenu.addAction(newAction)
		fileMenu.addSeparator()
		fileMenu.addAction(exitAction)

		editMenu = menubar.addMenu('Edit')
		copyAction = QAction('Copy',self)
		copyAction.setStatusTip('Copy content')
		pasteAction = QAction('Paste',self)
		pasteAction.setStatusTip('Paste content')
		editMenu.addAction(copyAction)
		editMenu.addAction(pasteAction)
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = GUI()
	gui.show()
	sys.exit(app.exec_())
