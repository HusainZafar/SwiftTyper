import time
import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from random import randrange

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

form_class = uic.loadUiType("type.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.begin()
	def begin(self):
		self.setupUi(self)
		self.show()
		passages = open('passages.json').read()
		self.para = json.loads(passages)['passages']
		global new,new1

		self.cur=self.output_para.textCursor()		
		self.cur.movePosition(QTextCursor.Start)
		format=self.cur.charFormat()
		format.setForeground(QtCore.Qt.yellow)
		self.cur.setCharFormat(format)
		self.cur.insertText(self.para[randrange(len(self.para))])
		self.cell1=(self.output_para.toPlainText())
		self.timer = QTimer(self)
		self.start_time = 60
		self.lcd_time.display("%02d:%02d" % (self.start_time/60,self.start_time % 60))
		self.restartTimer()
		self.timer.timeout.connect(self.updateLCD)
		self.count1=0
		self.count2=0
		self.input_para.textChanged[str].connect(self.done_typing_clicked)		
		self.cur.movePosition(QTextCursor.Start)		
		self.words=0
		self.acc=0			
		self.correct_char=0
		self.wrong_char=0		
		self.all_char=0
		self.net_wpm=0
		self.counter=0
		self.compensate=0			
		self.correct_char1=0
		self.wrong_char1=0		
		self.all_char1=0
		self.counter1=0
		self.compensate1=0
		self.count11=0
		self.count21=0	
		self.cur.deleteChar()		
		fmt=self.cur.charFormat()		
		fmt.setFontUnderline(True)		
		self.cur.setCharFormat(fmt)
		self.cur.insertText(self.cell1[self.count2])
		self.cur.movePosition(QTextCursor.Start)		
		
	def new_function(self):
			self.output_para.clear()
			self.cur.movePosition(QTextCursor.Start)
			format=self.cur.charFormat()
			format.setForeground(QtCore.Qt.yellow)
			self.cur.setCharFormat(format)
			self.r=randrange(len(self.para))
			self.cur.insertText(self.para[self.r])		
			self.cell1=(self.output_para.toPlainText())	
			self.cur.movePosition(QTextCursor.Start)			
			self.words=0
			self.acc=0			
			self.correct_char=0
			self.wrong_char=0		
			self.all_char=0
			self.counter=0
			self.compensate=0
			self.count1=0
			self.count2=0		

	def done_typing_clicked(self,text):
		new=text
		new1=text[-1]	
		if((len(new)-1)<self.count1):
			self.count1-=1
			self.count11-=1
			self.compensate+=1
			self.compensate1+=1
			return			
		elif(new1==self.cell1[self.count2]):
			self.correct_char+=1
			self.correct_char1+=1
			
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(True)			
			format.setForeground(QtCore.Qt.green)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			
			self.cur.movePosition(QTextCursor.Left)			
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(False)			
			format.setForeground(QtCore.Qt.green)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(True)			
			format.setForeground(QtCore.Qt.white)
			self.cur.setCharFormat(format)
			if(self.all_char>=(len(self.cell1))-1):
				self.cur.insertText(self.cell1[self.count2])
			else:
				self.cur.insertText(self.cell1[self.count2+1])
			self.cur.movePosition(QTextCursor.Left)
			
			self.count1+=1
			self.count11+=1
			self.count21+=1
			self.count2+=1
		elif(new1!=self.cell1[self.count2]):
			self.wrong_char+=1
			self.wrong_char1+=1			

			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(True)			
			format.setForeground(QtCore.Qt.red)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			
			self.cur.movePosition(QTextCursor.Left)			
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(False)			
			format.setForeground(QtCore.Qt.red)
			self.cur.setCharFormat(format)
			self.cur.insertText(self.cell1[self.count2])
			
			self.cur.deleteChar()			
			format=self.cur.charFormat()
			format.setFontUnderline(True)			
			format.setForeground(QtCore.Qt.white)
			self.cur.setCharFormat(format)

			if(self.all_char>=(len(self.cell1))-1):
				self.cur.insertText(self.cell1[self.count2])			
			else:
				self.cur.insertText(self.cell1[self.count2+1])
			self.cur.movePosition(QTextCursor.Left)

			self.count1+=1
			self.count11+=1
			self.count2+=1
			self.count21+=1
		self.all_char+=1 			
		self.all_char1+=1				
		tot=len(text)+self.compensate
		tot=len(text)+self.compensate1
		self.acc=float(self.correct_char1)/tot*100	
		self.words=self.all_char1/5.0		
		if(self.all_char>=(len(self.cell1))):
			self.new_function()
		

	def restartTimer(self):
		self.timer.stop()
		self.start_time = 60
		self.lcd_time.display("%d:%02d" % (self.start_time/60,self.start_time % 60))
		self.timer.start(1000)
		

	def show_message(self, title, text):
		box = QMessageBox(self)
		box.setWindowTitle(title)
		box.setText(text)
		box.setWindowFlags(box.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint & ~QtCore.Qt.WindowMinimizeButtonHint & ~QtCore.Qt.WindowCloseButtonHint)
		box.exec_()

	def updateLCD(self):
		if self.counter1==0:
			self.counter1+=1
			self.show_message('Swift Typer','Press OK when you are ready.')
		self.start_time -= 1
		if self.start_time >= 0:
			self.lcd_time.display("%d:%02d" % (self.start_time/60,self.start_time % 60))
			a=60-self.start_time
			elapsed = str(a)+".0"
			self.gross_wpm=float(self.words)*60.0/float(elapsed)
			self.lcd_accuracy.display(self.acc)
			self.net_wpm=float(self.gross_wpm-(self.wrong_char1/5.0)*60.0/(float(elapsed)))
			self.lcd_wpm.display(self.net_wpm)
		else:
			self.timer.stop()
			self.net_wpm=self.gross_wpm-(self.wrong_char1/5)
			self.show_message('TIME\'S UP!!!','Time\'s up. Press OK to see your final SCORE!!!')
			self.show_message('SCORE','Accuracy	:	%d\n\nWPM	:	%d' %(self.acc,self.net_wpm))

app = QtWidgets.QApplication(sys.argv)
myWindow = MyWindowClass()
sys.exit(app.exec_())
