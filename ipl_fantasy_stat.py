'''
Paduchuri Manideep
Basic Statistics of IPL Fantasy League PDF File for Educational Purpose. Don't misuse it.
'''
import sys
import os
import datetime
import tabula
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtWidgets import QApplication as QApp
from PyQt5.QtWidgets import QFileDialog as QFile
from PyQt5.QtWidgets import QWidget as QWid
from PyQt5.QtGui import QIcon as Qico
from PyQt5.QtWidgets import QCheckBox as QCheck
from PyQt5.QtWidgets import QLineEdit as QText
from PyQt5.QtWidgets import QMainWindow as QMWin
from PyQt5.QtWidgets import QLabel as QLbl
from PyQt5.QtWidgets import QPushButton as QBtn
from PyQt5.QtWidgets import QGridLayout as Grid
output_file_name = ""
def convertor(file_path):
	'''Converts PDF file to CSV File'''
	global output_file_name
	file_name = ""
	members = ""
	if '/' in file_path:
		file_path_list = file_path.split("/")
		file_name = file_path_list[-1]
		output_dup_name = file_name.split(".")[0]+".csv"
		output_org_name = file_name.split(".")[0]+"-org.csv"
	else:
		file_name = file_path
		output_dup_name = file_path.split(".")[0]+".csv"
		output_org_name = file_path.split(".")[0]+"-org.csv"
	tabula.convert_into(file_path,output_dup_name, pages="all",output_format="csv",guess = False, pandas_options={'header': 0})
	reader = open(output_dup_name,"r")
	writer = open(output_org_name,"w")
	output_file_name = output_dup_name
	writer.write("Team,Captain,ViceCaptain,Player1,Player2,Player3,Player4,Player5,Player6,Player7,Player7,Player8.Player9,Player10,Player11\n")
	for i in reader:
		if "User" in i:
			continue
		if "Members" in i:
			continue
		writer.write(i)
	reader.close()
	reader = open(output_dup_name,"r")
	for i in reader:
		members = i.split(",")[4].split(":")[1].strip()
		break
	os.remove(output_dup_name)
	os.rename(output_org_name,output_dup_name)
	writer.close()
	reader.close()
	now = datetime.datetime.now()
	date_now = now.strftime("%Y-%m-%d %H:%M:%S")
	log_file = open("ipl_stats.log","a")	
	log_file.write("["+date_now+"]"+" \"Converted IPL PDF File "+file_name+" to "+file_name[:-4]+".csv File\"\n")
	log_file.close()
	return (members,output_dup_name)
def image_captains(file_path,members):
	'''Generates Statistics on Captain Column'''
	plt.style.use('ggplot')
	data = pd.read_csv(file_path)
	ax = data['Captain'].value_counts().plot(kind='barh', figsize=(20,6),color="coral", fontsize=9);
	plt.subplots_adjust(bottom=0.4)
	plt.subplots_adjust(top=0.7)
	ax.text(1, 1, "Out of "+str(members)+" Teams", transform=ax.transAxes, fontsize=14,verticalalignment='top')
	for i in ax.patches:
	    ax.text(i.get_width()+.3, i.get_y()+.38,str(i.get_width()), fontsize=8,color='dimgrey')
	plt.subplots_adjust(left=0.3, right=0.9, top=0.99, bottom=0.0)
	ax.invert_yaxis()
	plt.savefig('captains.png')
	plt.clf()
	now = datetime.datetime.now()
	date_now = now.strftime("%Y-%m-%d %H:%M:%S")
	log_file = open("ipl_stats.log","a")
	log_file.write("["+date_now+"]"+" \"Generated Captain Statistics for "+output_file_name[:-4]+".pdf\"\n")
	log_file.close()
def image_viceCaptains(file_path,members):
	'''Generates Statistics on ViceCaptain Column'''
	plt.style.use('ggplot')
	data = pd.read_csv(file_path)
	ax = data['ViceCaptain'].value_counts().plot(kind='barh', figsize=(20,6),
		                                color="coral", fontsize=9);
	plt.subplots_adjust(bottom=0.4)
	plt.subplots_adjust(top=0.7)
	ax.text(1, 1,"Out of "+str(members)+" Teams", transform=ax.transAxes, fontsize=14,verticalalignment='top')
	for i in ax.patches:
	    ax.text(i.get_width()+1.0, i.get_y()+.38,str(i.get_width()), fontsize=8,color='dimgrey')
	plt.subplots_adjust(left=0.3, right=0.9, top=0.99, bottom=0.0)
	ax.invert_yaxis()
	plt.savefig('vice_Captains.png')
	plt.clf()
	now = datetime.datetime.now()
	date_now = now.strftime("%Y-%m-%d %H:%M:%S")
	log_file = open("ipl_stats.log","a")
	log_file.write("["+date_now+"]"+" \"Generated Vice-Captain Statistics for "+output_file_name[:-4]+".pdf\"\n")
	log_file.close()
def all_players_img(file_path,members):
	'''Generates Statistics on count of each player in Teams'''
	plt.style.use('ggplot')
	all_players = []
	count = 1
	reader = open(file_path,"r")
	for i in reader:
		if count == 1:
			count = 0
			continue
		list_line = i.strip().split(",")
		list_line = list_line[1:]
		for j in list_line:
			all_players.append(j)
	data_frame = pd.DataFrame({'all_players':all_players})	
	ax = data_frame['all_players'].value_counts().plot(kind='barh', figsize=(20,6),
		                                color="coral", fontsize=9);
	ax.text(1, 1, "Out of "+str(members)+" Teams", transform=ax.transAxes, fontsize=14,verticalalignment='top')
	plt.subplots_adjust(bottom=0.4)
	plt.subplots_adjust(top=0.7)

	for i in ax.patches:
	    ax.text(i.get_width()+.3, i.get_y()+.38,str(i.get_width()), fontsize=8,color='dimgrey')
	plt.subplots_adjust(left=0.3, right=0.9, top=0.99, bottom=0.0)
	ax.invert_yaxis()
	plt.savefig('all_players.png')
	plt.clf()
	reader.close()
	now = datetime.datetime.now()
	date_now = now.strftime("%Y-%m-%d %H:%M:%S")
	log_file = open("ipl_stats.log","a")	
	log_file.write("["+date_now+"]"+" \"Generated All Players Statistics for "+output_file_name[:-4]+".pdf\"\n")
	log_file.close()
class App(QWid):
	'''Class for GUI Window'''
	file_path = ""
	def __init__(self):
		super().__init__()
		self.title = "IPL Fantasy League Stats"
		self.showMaximized()
		self.initUI()
	def initUI(self):
		self.setWindowIcon(Qico('pythonlogo.png'))
		self.setWindowTitle(self.title)
		self.SetWidgets()
		self.show()
	def SetWidgets(self):
		#Grid Layout
		self.layout = Grid()
		for i in range(0,11):
			self.layout.setColumnStretch(i,9)
		for i in range(0,12):
			self.layout.setRowStretch(i,12)
		self.label = QLbl("IPL Fantasy League Analysis Stats")
		self.label.setStyleSheet('''QLabel{font-size:30px;font-weight:bold;text-align:center;}''')
		self.layout.addWidget(self.label,0,3,3,3)
		self.btn1 = QBtn("Open File")
		self.btn1.clicked.connect(self.getfiles)
		self.layout.addWidget(self.btn1,2,5,2,2)
		self.textbox = QText(self)
		self.layout.addWidget(self.textbox,2,3,2,2)
		self.captains = QCheck("Captain Stats",self)
		self.vice_captains = QCheck("ViceCaptain Stats",self)
		self.player = QCheck("Players Stats",self)
		self.layout.addWidget(self.captains,3,3,2,1)
		self.layout.addWidget(self.vice_captains,3,4,2,1)
		self.layout.addWidget(self.player,3,5,2,2)
		self.submit = QBtn("Submit")
		self.submit.clicked.connect(self.submitter)
		self.layout.addWidget(self.submit,4,4,2,2)
		self.setLayout(self.layout)
		#End of Grid Layout
	def submitter(self):
		if self.file_path != '':
			mem, output_csv = convertor(self.file_path)
			if self.player.isChecked():
				all_players_img(output_csv,mem)
			if self.captains.isChecked():
				image_captains(output_csv,mem)
			if self.vice_captains.isChecked():
				image_viceCaptains(output_csv,mem)
			self.player.setChecked(False)
			self.vice_captains.setChecked(False)
			self.captains.setChecked(False)
			self.textbox.setText("")
	def getfiles(self):
		options = QFile.Options()
		options |= QFile.DontUseNativeDialog
		fileName, _ = QFile.getOpenFileName(self,"Select IPL Fantasy PDF File", "","PDF Files (*.pdf)", options=options)
		if fileName:
			self.file_path = fileName
		self.textbox.setText(fileName)
app_obj = QApp(sys.argv)
execute = App()
sys.exit(app_obj.exec_())