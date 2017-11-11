# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnimationPlayerWindow(object):
    def setupUi(self, AnimationPlayerWindow):
        AnimationPlayerWindow.setObjectName("AnimationPlayerWindow")
        AnimationPlayerWindow.resize(600, 400)
        self.animation_player = QtWidgets.QWidget(AnimationPlayerWindow)
        self.animation_player.setObjectName("animation_player")
        self.gridLayout = QtWidgets.QGridLayout(self.animation_player)
        self.gridLayout.setObjectName("gridLayout")
        self.play_button = QtWidgets.QPushButton(self.animation_player)
        self.play_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setMinimumSize(QtCore.QSize(72, 32))
        self.play_button.setMaximumSize(QtCore.QSize(72, 32))
        self.play_button.setObjectName("play_button")
        self.gridLayout.addWidget(self.play_button, 1, 0, 1, 1)
        self.stop_button = QtWidgets.QPushButton(self.animation_player)
        self.stop_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setMinimumSize(QtCore.QSize(72, 32))
        self.stop_button.setMaximumSize(QtCore.QSize(72, 32))
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 1, 1, 1, 1)
        self.slider = QtWidgets.QSlider(self.animation_player)
        self.slider.setEnabled(False)
        self.slider.setMinimumSize(QtCore.QSize(0, 22))
        self.slider.setMaximumSize(QtCore.QSize(16777215, 22))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout.addWidget(self.slider, 1, 2, 1, 1)
        self.viewer = AnimationPlayerViewer(self.animation_player)
        self.viewer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);")
        self.viewer.setObjectName("viewer")
        self.gridLayout.addWidget(self.viewer, 0, 0, 1, 3)
        AnimationPlayerWindow.setCentralWidget(self.animation_player)
        self.AnimationPlayerMenu = QtWidgets.QMenuBar(AnimationPlayerWindow)
        self.AnimationPlayerMenu.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.AnimationPlayerMenu.setNativeMenuBar(False)
        self.AnimationPlayerMenu.setObjectName("AnimationPlayerMenu")
        self.menu_file = QtWidgets.QMenu(self.AnimationPlayerMenu)
        self.menu_file.setObjectName("menu_file")
        AnimationPlayerWindow.setMenuBar(self.AnimationPlayerMenu)
        self.action_open = QtWidgets.QAction(AnimationPlayerWindow)
        self.action_open.setObjectName("action_open")
        self.menu_file.addAction(self.action_open)
        self.AnimationPlayerMenu.addAction(self.menu_file.menuAction())

        self.retranslateUi(AnimationPlayerWindow)
        QtCore.QMetaObject.connectSlotsByName(AnimationPlayerWindow)

    def retranslateUi(self, AnimationPlayerWindow):
        _translate = QtCore.QCoreApplication.translate
        AnimationPlayerWindow.setWindowTitle(_translate("AnimationPlayerWindow", "Point Animation"))
        self.play_button.setText(_translate("AnimationPlayerWindow", "Play"))
        self.stop_button.setText(_translate("AnimationPlayerWindow", "Stop"))
        self.menu_file.setTitle(_translate("AnimationPlayerWindow", "File"))
        self.action_open.setText(_translate("AnimationPlayerWindow", "Open"))

from animationplayer import AnimationPlayerViewer
