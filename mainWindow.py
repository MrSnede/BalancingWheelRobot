# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainWindow.ui'
#
# Created: Sat Nov 29 18:47:56 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1237, 745)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Serial_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.Serial_groupBox.setObjectName(_fromUtf8("Serial_groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Serial_groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.HLayOutSerialSettings = QtGui.QHBoxLayout()
        self.HLayOutSerialSettings.setObjectName(_fromUtf8("HLayOutSerialSettings"))
        self.portsComboBox = QtGui.QComboBox(self.Serial_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portsComboBox.sizePolicy().hasHeightForWidth())
        self.portsComboBox.setSizePolicy(sizePolicy)
        self.portsComboBox.setMinimumSize(QtCore.QSize(100, 27))
        self.portsComboBox.setObjectName(_fromUtf8("portsComboBox"))
        self.HLayOutSerialSettings.addWidget(self.portsComboBox)
        self.refreshPortsPushButton = QtGui.QPushButton(self.Serial_groupBox)
        self.refreshPortsPushButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshPortsPushButton.sizePolicy().hasHeightForWidth())
        self.refreshPortsPushButton.setSizePolicy(sizePolicy)
        self.refreshPortsPushButton.setMinimumSize(QtCore.QSize(38, 27))
        self.refreshPortsPushButton.setMaximumSize(QtCore.QSize(38, 27))
        self.refreshPortsPushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshPortsPushButton.setIcon(icon)
        self.refreshPortsPushButton.setIconSize(QtCore.QSize(16, 16))
        self.refreshPortsPushButton.setObjectName(_fromUtf8("refreshPortsPushButton"))
        self.HLayOutSerialSettings.addWidget(self.refreshPortsPushButton)
        self.baudRateComboBox = QtGui.QComboBox(self.Serial_groupBox)
        self.baudRateComboBox.setMinimumSize(QtCore.QSize(91, 27))
        self.baudRateComboBox.setObjectName(_fromUtf8("baudRateComboBox"))
        self.HLayOutSerialSettings.addWidget(self.baudRateComboBox)
        self.connectPushButton = QtGui.QPushButton(self.Serial_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectPushButton.sizePolicy().hasHeightForWidth())
        self.connectPushButton.setSizePolicy(sizePolicy)
        self.connectPushButton.setMinimumSize(QtCore.QSize(91, 27))
        self.connectPushButton.setObjectName(_fromUtf8("connectPushButton"))
        self.HLayOutSerialSettings.addWidget(self.connectPushButton)
        self.disconnectPushButton = QtGui.QPushButton(self.Serial_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectPushButton.sizePolicy().hasHeightForWidth())
        self.disconnectPushButton.setSizePolicy(sizePolicy)
        self.disconnectPushButton.setMinimumSize(QtCore.QSize(91, 27))
        self.disconnectPushButton.setObjectName(_fromUtf8("disconnectPushButton"))
        self.HLayOutSerialSettings.addWidget(self.disconnectPushButton)
        self.verticalLayout.addLayout(self.HLayOutSerialSettings)
        self.logPlainTextEdit = QtGui.QPlainTextEdit(self.Serial_groupBox)
        self.logPlainTextEdit.setMinimumSize(QtCore.QSize(270, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.logPlainTextEdit.setFont(font)
        self.logPlainTextEdit.setReadOnly(True)
        self.logPlainTextEdit.setObjectName(_fromUtf8("logPlainTextEdit"))
        self.verticalLayout.addWidget(self.logPlainTextEdit)
        self.cmdLineEdit = QtGui.QLineEdit(self.Serial_groupBox)
        self.cmdLineEdit.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.cmdLineEdit.setFont(font)
        self.cmdLineEdit.setDragEnabled(True)
        self.cmdLineEdit.setPlaceholderText(_fromUtf8(""))
        self.cmdLineEdit.setObjectName(_fromUtf8("cmdLineEdit"))
        self.verticalLayout.addWidget(self.cmdLineEdit)
        self.horizontalLayout_2.addWidget(self.Serial_groupBox)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.PID_groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.PID_groupBox_2.setObjectName(_fromUtf8("PID_groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.PID_groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.D_Label = QtGui.QLabel(self.PID_groupBox_2)
        self.D_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.D_Label.setObjectName(_fromUtf8("D_Label"))
        self.gridLayout.addWidget(self.D_Label, 2, 0, 1, 1)
        self.I_Label = QtGui.QLabel(self.PID_groupBox_2)
        self.I_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.I_Label.setObjectName(_fromUtf8("I_Label"))
        self.gridLayout.addWidget(self.I_Label, 1, 0, 1, 1)
        self.P_ValueLabel = QtGui.QLabel(self.PID_groupBox_2)
        self.P_ValueLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.P_ValueLabel.setText(_fromUtf8(""))
        self.P_ValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.P_ValueLabel.setObjectName(_fromUtf8("P_ValueLabel"))
        self.gridLayout.addWidget(self.P_ValueLabel, 0, 1, 1, 1)
        self.I_ValueLabel = QtGui.QLabel(self.PID_groupBox_2)
        self.I_ValueLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.I_ValueLabel.setText(_fromUtf8(""))
        self.I_ValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.I_ValueLabel.setObjectName(_fromUtf8("I_ValueLabel"))
        self.gridLayout.addWidget(self.I_ValueLabel, 1, 1, 1, 1)
        self.P_HSlider = QtGui.QSlider(self.PID_groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_HSlider.sizePolicy().hasHeightForWidth())
        self.P_HSlider.setSizePolicy(sizePolicy)
        self.P_HSlider.setMaximum(3000)
        self.P_HSlider.setSingleStep(100)
        self.P_HSlider.setPageStep(300)
        self.P_HSlider.setProperty("value", 2000)
        self.P_HSlider.setOrientation(QtCore.Qt.Horizontal)
        self.P_HSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.P_HSlider.setTickInterval(100)
        self.P_HSlider.setObjectName(_fromUtf8("P_HSlider"))
        self.gridLayout.addWidget(self.P_HSlider, 0, 2, 1, 1)
        self.D_ValueLabel = QtGui.QLabel(self.PID_groupBox_2)
        self.D_ValueLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.D_ValueLabel.setText(_fromUtf8(""))
        self.D_ValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.D_ValueLabel.setObjectName(_fromUtf8("D_ValueLabel"))
        self.gridLayout.addWidget(self.D_ValueLabel, 2, 1, 1, 1)
        self.P_Label = QtGui.QLabel(self.PID_groupBox_2)
        self.P_Label.setMinimumSize(QtCore.QSize(20, 0))
        self.P_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.P_Label.setObjectName(_fromUtf8("P_Label"))
        self.gridLayout.addWidget(self.P_Label, 0, 0, 1, 1)
        self.D_HSlider = QtGui.QSlider(self.PID_groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.D_HSlider.sizePolicy().hasHeightForWidth())
        self.D_HSlider.setSizePolicy(sizePolicy)
        self.D_HSlider.setMaximum(3000)
        self.D_HSlider.setSingleStep(100)
        self.D_HSlider.setPageStep(300)
        self.D_HSlider.setProperty("value", 2000)
        self.D_HSlider.setOrientation(QtCore.Qt.Horizontal)
        self.D_HSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.D_HSlider.setTickInterval(100)
        self.D_HSlider.setObjectName(_fromUtf8("D_HSlider"))
        self.gridLayout.addWidget(self.D_HSlider, 2, 2, 1, 1)
        self.I_HSlider = QtGui.QSlider(self.PID_groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.I_HSlider.sizePolicy().hasHeightForWidth())
        self.I_HSlider.setSizePolicy(sizePolicy)
        self.I_HSlider.setMaximum(3000)
        self.I_HSlider.setSingleStep(100)
        self.I_HSlider.setPageStep(300)
        self.I_HSlider.setProperty("value", 2000)
        self.I_HSlider.setOrientation(QtCore.Qt.Horizontal)
        self.I_HSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.I_HSlider.setTickInterval(100)
        self.I_HSlider.setObjectName(_fromUtf8("I_HSlider"))
        self.gridLayout.addWidget(self.I_HSlider, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.PID_groupBox_2)
        self.FreeSlider_groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.FreeSlider_groupBox_3.setObjectName(_fromUtf8("FreeSlider_groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.FreeSlider_groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.FreeSlider2_Label = QtGui.QLabel(self.FreeSlider_groupBox_3)
        self.FreeSlider2_Label.setObjectName(_fromUtf8("FreeSlider2_Label"))
        self.gridLayout_2.addWidget(self.FreeSlider2_Label, 1, 0, 1, 1)
        self.FreeSlider1_Label = QtGui.QLabel(self.FreeSlider_groupBox_3)
        self.FreeSlider1_Label.setObjectName(_fromUtf8("FreeSlider1_Label"))
        self.gridLayout_2.addWidget(self.FreeSlider1_Label, 0, 0, 1, 1)
        self.FreeSlider2_HSlider = QtGui.QSlider(self.FreeSlider_groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FreeSlider2_HSlider.sizePolicy().hasHeightForWidth())
        self.FreeSlider2_HSlider.setSizePolicy(sizePolicy)
        self.FreeSlider2_HSlider.setMaximum(3000)
        self.FreeSlider2_HSlider.setSingleStep(100)
        self.FreeSlider2_HSlider.setPageStep(300)
        self.FreeSlider2_HSlider.setProperty("value", 2000)
        self.FreeSlider2_HSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FreeSlider2_HSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.FreeSlider2_HSlider.setTickInterval(100)
        self.FreeSlider2_HSlider.setObjectName(_fromUtf8("FreeSlider2_HSlider"))
        self.gridLayout_2.addWidget(self.FreeSlider2_HSlider, 1, 2, 1, 1)
        self.FreeSlider2_ValueLabel = QtGui.QLabel(self.FreeSlider_groupBox_3)
        self.FreeSlider2_ValueLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.FreeSlider2_ValueLabel.setText(_fromUtf8(""))
        self.FreeSlider2_ValueLabel.setObjectName(_fromUtf8("FreeSlider2_ValueLabel"))
        self.gridLayout_2.addWidget(self.FreeSlider2_ValueLabel, 1, 1, 1, 1)
        self.FreeSlider1_HSlider = QtGui.QSlider(self.FreeSlider_groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FreeSlider1_HSlider.sizePolicy().hasHeightForWidth())
        self.FreeSlider1_HSlider.setSizePolicy(sizePolicy)
        self.FreeSlider1_HSlider.setMaximum(3000)
        self.FreeSlider1_HSlider.setSingleStep(100)
        self.FreeSlider1_HSlider.setPageStep(300)
        self.FreeSlider1_HSlider.setProperty("value", 2000)
        self.FreeSlider1_HSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FreeSlider1_HSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.FreeSlider1_HSlider.setTickInterval(100)
        self.FreeSlider1_HSlider.setObjectName(_fromUtf8("FreeSlider1_HSlider"))
        self.gridLayout_2.addWidget(self.FreeSlider1_HSlider, 0, 2, 1, 1)
        self.FreeSlider1_ValueLabel = QtGui.QLabel(self.FreeSlider_groupBox_3)
        self.FreeSlider1_ValueLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.FreeSlider1_ValueLabel.setText(_fromUtf8(""))
        self.FreeSlider1_ValueLabel.setObjectName(_fromUtf8("FreeSlider1_ValueLabel"))
        self.gridLayout_2.addWidget(self.FreeSlider1_ValueLabel, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.FreeSlider_groupBox_3)
        self.FreeSwitches_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.FreeSwitches_groupBox.setObjectName(_fromUtf8("FreeSwitches_groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.FreeSwitches_groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Free_Free_checkBox_1 = QtGui.QCheckBox(self.FreeSwitches_groupBox)
        self.Free_Free_checkBox_1.setObjectName(_fromUtf8("Free_Free_checkBox_1"))
        self.horizontalLayout.addWidget(self.Free_Free_checkBox_1)
        self.Free_checkBox_2 = QtGui.QCheckBox(self.FreeSwitches_groupBox)
        self.Free_checkBox_2.setObjectName(_fromUtf8("Free_checkBox_2"))
        self.horizontalLayout.addWidget(self.Free_checkBox_2)
        self.Free_checkBox_3 = QtGui.QCheckBox(self.FreeSwitches_groupBox)
        self.Free_checkBox_3.setObjectName(_fromUtf8("Free_checkBox_3"))
        self.horizontalLayout.addWidget(self.Free_checkBox_3)
        self.Free_checkBox_4 = QtGui.QCheckBox(self.FreeSwitches_groupBox)
        self.Free_checkBox_4.setObjectName(_fromUtf8("Free_checkBox_4"))
        self.horizontalLayout.addWidget(self.Free_checkBox_4)
        self.Free_checkBox_5 = QtGui.QCheckBox(self.FreeSwitches_groupBox)
        self.Free_checkBox_5.setObjectName(_fromUtf8("Free_checkBox_5"))
        self.horizontalLayout.addWidget(self.Free_checkBox_5)
        self.verticalLayout_2.addWidget(self.FreeSwitches_groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.mpl_widget = MplWidget(self.centralwidget)
        self.mpl_widget.setMinimumSize(QtCore.QSize(0, 300))
        self.mpl_widget.setObjectName(_fromUtf8("mpl_widget"))
        self.verticalLayout_3.addWidget(self.mpl_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1237, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QObject.connect(self.cmdLineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.logPlainTextEdit.paste)
        QtCore.QObject.connect(self.P_HSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.P_ValueLabel.setNum)
        QtCore.QObject.connect(self.I_HSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.I_ValueLabel.setNum)
        QtCore.QObject.connect(self.D_HSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.D_ValueLabel.setNum)
        QtCore.QObject.connect(self.FreeSlider1_HSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.FreeSlider1_ValueLabel.setNum)
        QtCore.QObject.connect(self.FreeSlider2_HSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.FreeSlider2_ValueLabel.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BotControlGUI", None))
        self.Serial_groupBox.setTitle(_translate("MainWindow", "Serielle Verbindung", None))
        self.connectPushButton.setText(_translate("MainWindow", "Connect", None))
        self.disconnectPushButton.setText(_translate("MainWindow", "Disconnect", None))
        self.cmdLineEdit.setText(_translate("MainWindow", ">LedBlinkTime=100<", None))
        self.PID_groupBox_2.setTitle(_translate("MainWindow", "PID Regler", None))
        self.D_Label.setText(_translate("MainWindow", "D :", None))
        self.I_Label.setText(_translate("MainWindow", "I :", None))
        self.P_Label.setText(_translate("MainWindow", "P :", None))
        self.FreeSlider_groupBox_3.setTitle(_translate("MainWindow", "Freie Regler", None))
        self.FreeSlider2_Label.setText(_translate("MainWindow", "Max Geschwindigkeit:", None))
        self.FreeSlider1_Label.setText(_translate("MainWindow", "Max Beschleunigung :", None))
        self.FreeSwitches_groupBox.setTitle(_translate("MainWindow", "Freie Schalter", None))
        self.Free_Free_checkBox_1.setText(_translate("MainWindow", "Schalter 1", None))
        self.Free_checkBox_2.setText(_translate("MainWindow", "Schalter 2", None))
        self.Free_checkBox_3.setText(_translate("MainWindow", "Schalter 3", None))
        self.Free_checkBox_4.setText(_translate("MainWindow", "Schalter 4", None))
        self.Free_checkBox_5.setText(_translate("MainWindow", "Schalter 5", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from mplwidget import MplWidget
import mainWindow_rc
