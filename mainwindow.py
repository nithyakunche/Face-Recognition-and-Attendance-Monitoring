# Modified by Augmented Startups & Geeky Bee
# October 2020
# Facial Recognition Attendence GUI
# Full Course - https://augmentedstartups.info/yolov4release
# *-
import sys
import time
import gdown
import glob
import os
import shutil
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QDialog, QSplashScreen
import resource
# from model import Model
from out_window import Ui_OutputDialog


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("mainwindow.ui", self)
        self.runButton.clicked.connect(self.runSlot)
        self._new_window = None
        self.Videocapture_ = None

    def refreshAll(self):
        """
        Set the text of lineEdit once it's valid
        """
        self.Videocapture_ = "0"

    @pyqtSlot()
    # @staticmethod
    def runSlot(self):
        """
        Called when the user presses the Run button
        """
        print("Clicked Run")
        self.refreshAll()
        print(self.Videocapture_)
        ui.hide()# hide the main window
        self.outputWindow_()# Create and open new output window

    def outputWindow_(self):
        """
        Created new window for vidual output of the video in GUI
        """

        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        splash = SplashScreen()
        splash.__init__()
        splash.show()
        splash.progress()
        self._new_window.startVideo(self.Videocapture_)
        print("Video Played")

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splash.ui", self)
        self.center()

    def progress(self):
        for i in range(100):
            time.sleep(0)
            self.progressBar.setValue(i)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
