# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_subnet_calculator2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.box_first_ip = QtWidgets.QLineEdit(self.frame_2)
        self.box_first_ip.setObjectName("box_first_ip")
        self.gridLayout_3.addWidget(self.box_first_ip, 5, 1, 1, 1)
        self.label_subnet = QtWidgets.QLabel(self.frame_2)
        self.label_subnet.setObjectName("label_subnet")
        self.gridLayout_3.addWidget(self.label_subnet, 4, 0, 1, 1)
        self.box_last_ip = QtWidgets.QLineEdit(self.frame_2)
        self.box_last_ip.setObjectName("box_last_ip")
        self.gridLayout_3.addWidget(self.box_last_ip, 6, 1, 1, 1)
        self.label_firstip = QtWidgets.QLabel(self.frame_2)
        self.label_firstip.setObjectName("label_firstip")
        self.gridLayout_3.addWidget(self.label_firstip, 5, 0, 1, 1)
        self.label_broadcastip = QtWidgets.QLabel(self.frame_2)
        self.label_broadcastip.setObjectName("label_broadcastip")
        self.gridLayout_3.addWidget(self.label_broadcastip, 7, 0, 1, 1)
        self.label_lastip = QtWidgets.QLabel(self.frame_2)
        self.label_lastip.setObjectName("label_lastip")
        self.gridLayout_3.addWidget(self.label_lastip, 6, 0, 1, 1)
        self.box_broadcast_ip = QtWidgets.QLineEdit(self.frame_2)
        self.box_broadcast_ip.setObjectName("box_broadcast_ip")
        self.gridLayout_3.addWidget(self.box_broadcast_ip, 7, 1, 1, 1)
        self.box_subnet_id = QtWidgets.QLineEdit(self.frame_2)
        self.box_subnet_id.setObjectName("box_subnet_id")
        self.gridLayout_3.addWidget(self.box_subnet_id, 4, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.box_subnet_id_binary = QtWidgets.QLineEdit(self.frame_3)
        self.box_subnet_id_binary.setObjectName("box_subnet_id_binary")
        self.gridLayout_4.addWidget(self.box_subnet_id_binary, 0, 0, 1, 1)
        self.box_last_ip_binary = QtWidgets.QLineEdit(self.frame_3)
        self.box_last_ip_binary.setObjectName("box_last_ip_binary")
        self.gridLayout_4.addWidget(self.box_last_ip_binary, 2, 0, 1, 1)
        self.box_broadcast_ip_binary = QtWidgets.QLineEdit(self.frame_3)
        self.box_broadcast_ip_binary.setObjectName("box_broadcast_ip_binary")
        self.gridLayout_4.addWidget(self.box_broadcast_ip_binary, 3, 0, 1, 1)
        self.box_first_ip_binary = QtWidgets.QLineEdit(self.frame_3)
        self.box_first_ip_binary.setObjectName("box_first_ip_binary")
        self.gridLayout_4.addWidget(self.box_first_ip_binary, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_3, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setEnabled(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_enterip = QtWidgets.QLabel(self.frame)
        self.label_enterip.setObjectName("label_enterip")
        self.gridLayout_2.addWidget(self.label_enterip, 0, 0, 1, 1)
        self.box_user_input = QtWidgets.QLineEdit(self.frame)
        self.box_user_input.setObjectName("box_user_input")
        self.gridLayout_2.addWidget(self.box_user_input, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.text_browser = QtWidgets.QTextBrowser(self.frame_4)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout_5.addWidget(self.text_browser, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Subnet Calculator"))
        self.box_first_ip.setStatusTip(_translate("MainWindow", "First usable host address"))
        self.label_subnet.setText(_translate("MainWindow", "Subnet ID:"))
        self.box_last_ip.setStatusTip(_translate("MainWindow", "Last usable host address"))
        self.label_firstip.setText(_translate("MainWindow", "First valid IP:"))
        self.label_broadcastip.setText(_translate("MainWindow", "Broadcast IP:"))
        self.label_lastip.setText(_translate("MainWindow", "Last valid IP:"))
        self.box_broadcast_ip.setStatusTip(_translate("MainWindow", "Broadcast address"))
        self.box_subnet_id.setStatusTip(_translate("MainWindow", "Subnetwork address"))
        self.label_enterip.setText(_translate("MainWindow", "Enter your IP/mask:"))
        self.box_user_input.setToolTip(_translate("MainWindow", "Enter your IP/mask combination here, e.g. 192.168.1.130/25"))
        self.box_user_input.setStatusTip(_translate("MainWindow", "Enter your IP and mask"))
        self.box_user_input.setPlaceholderText(_translate("MainWindow", "Ex: 192.168.1.10/24"))

