from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
import os
from bs4 import BeautifulSoup
import requests

class imdb(QWidget):

    def __init__(self):
        super().__init__()
        self.Interface()

    def Interface(self):
        self.title = "Python IMDB Top 250"
        self.setWindowTitle(self.title)
        self.logo = QLabel()
        self.logo.setPixmap(QtGui.QPixmap("logo.jpg")) #Load İmages
        self.textEdit01 = QTextEdit()

        self.checkboxTop50 = QCheckBox("Top 50")
        self.checkboxTop100 = QCheckBox("Top 100")
        self.checkboxTop150 = QCheckBox("Top 150")
        self.checkboxTop200 = QCheckBox("Top 200")
        self.checkboxTop250 = QCheckBox("Top 250")

        self.buttonGet = QPushButton("Get List!")
        self.buttonClear = QPushButton("Clear")
        self.buttonSave = QPushButton("Save")

        horizonBoxForLogo = QHBoxLayout()
        horizonBoxForLogo.addWidget(self.logo)

        verticalBoxForText = QVBoxLayout()
        verticalBoxForText.addWidget(self.textEdit01)

        horizonBoxForBox = QHBoxLayout()
        horizonBoxForBox.addWidget(self.checkboxTop50)
        horizonBoxForBox.addWidget(self.checkboxTop100)
        horizonBoxForBox.addWidget(self.checkboxTop150)
        horizonBoxForBox.addWidget(self.checkboxTop200)
        horizonBoxForBox.addWidget(self.checkboxTop250)

        horizonBoxForButtons = QHBoxLayout()
        horizonBoxForButtons.addWidget(self.buttonGet)
        horizonBoxForButtons.addWidget(self.buttonClear)
        horizonBoxForButtons.addWidget(self.buttonSave)

        verticalBoxForLeft = QVBoxLayout()
        verticalBoxForLeft.addLayout(verticalBoxForText)
        verticalBoxForLeft.addLayout(horizonBoxForBox)
        verticalBoxForLeft.addLayout(horizonBoxForButtons)

        horizonBoxForWindow = QHBoxLayout()
        horizonBoxForWindow.addLayout(horizonBoxForLogo)
        horizonBoxForWindow.addLayout(verticalBoxForLeft)


        self.buttonGet.clicked.connect(lambda : self.whenClicked(self.checkboxTop50.isChecked(), self.checkboxTop100.isChecked(),self.checkboxTop150.isChecked(),self.checkboxTop200.isChecked(),self.checkboxTop250.isChecked()))
        self.buttonClear.clicked.connect(self.clearSave)
        self.buttonSave.clicked.connect(self.clearSave)

        self.setLayout(horizonBoxForWindow)
        self.show()

    def getInfos(self,url):

        response = requests.get(url)
        content = response.content
        bringIt = BeautifulSoup(content,"html.parser")

        for movies in bringIt.find_all("h3",{"class": "lister-item-header"}):
            self.textEdit01.append(movies.text)

    def whenClicked(self,checkboxTop50,checkboxTop100,checkboxTop150,checkboxTop200,checkboxTop250):

        if checkboxTop50:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
        elif checkboxTop100:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
        elif checkboxTop150:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
        elif checkboxTop200:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt")
        elif checkboxTop250:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt")

    def clearSave(self):
        sender = self.sender()

        if sender.text() == "Clear":
            self.textEdit01.clear()
        elif sender.text() ==  "Save":
            fileWay = QFileDialog.getSaveFileName(self,"Save...",os.getenv("HOME"))
            userFile = open(fileWay[0],"w",encoding="utf-8")
            userFile.write(self.textEdit01.toPlainText())
            userFile.close()

myApp = QApplication(sys.argv)
createIt = imdb()
sys.exit(myApp.exec())
