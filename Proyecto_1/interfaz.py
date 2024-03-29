from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(940, 701)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/1.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(parent=self.frame)
        self.logo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Images/1.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.logo.setOpenExternalLinks(False)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_inicio = QtWidgets.QPushButton(parent=self.frame_4)
        self.bt_inicio.setMinimumSize(QtCore.QSize(80, 50))
        self.bt_inicio.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000000ff;\n"
            "border-radius:20px\n"
            "}")
        self.bt_inicio.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/inicio.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_inicio.setIcon(icon1)
        self.bt_inicio.setIconSize(QtCore.QSize(100, 60))
        self.bt_inicio.setShortcut("")
        self.bt_inicio.setCheckable(False)
        self.bt_inicio.setAutoRepeat(False)
        self.bt_inicio.setAutoExclusive(False)
        self.bt_inicio.setObjectName("bt_inicio")
        self.horizontalLayout_4.addWidget(self.bt_inicio)
        self.bt_comics = QtWidgets.QPushButton(parent=self.frame_4)
        self.bt_comics.setMinimumSize(QtCore.QSize(80, 50))
        self.bt_comics.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000000ff;\n"
            "border-radius:20px\n"
            "}\n"
            "")
        self.bt_comics.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/comics.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_comics.setIcon(icon2)
        self.bt_comics.setIconSize(QtCore.QSize(100, 60))
        self.bt_comics.setObjectName("bt_comics")
        self.horizontalLayout_4.addWidget(self.bt_comics)
        self.bt_personajes = QtWidgets.QPushButton(parent=self.frame_4)
        self.bt_personajes.setMinimumSize(QtCore.QSize(80, 50))
        self.bt_personajes.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000000ff;\n"
            "border-radius:20px\n"
            "}\n"
            "")
        self.bt_personajes.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/personaje.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_personajes.setIcon(icon3)
        self.bt_personajes.setIconSize(QtCore.QSize(100, 60))
        self.bt_personajes.setObjectName("bt_personajes")
        self.horizontalLayout_4.addWidget(self.bt_personajes)
        self.bt_info = QtWidgets.QPushButton(parent=self.frame_4)
        self.bt_info.setMinimumSize(QtCore.QSize(80, 50))
        self.bt_info.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000000ff;\n"
            "border-radius:20px\n"
            "}\n"
            "")
        self.bt_info.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/info.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_info.setIcon(icon4)
        self.bt_info.setIconSize(QtCore.QSize(100, 60))
        self.bt_info.setObjectName("bt_info")
        self.horizontalLayout_4.addWidget(self.bt_info)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(15, 0, 0, 100)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_min = QtWidgets.QPushButton(parent=self.frame_5)
        self.bt_min.setMinimumSize(QtCore.QSize(35, 35))
        self.bt_min.setMaximumSize(QtCore.QSize(35, 35))
        self.bt_min.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000000ff;\n"
            "border-radius:20px\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(170, 170, 255);\n"
            "border-radius:20px\n"
            "}")
        self.bt_min.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/Minimize.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_min.setIcon(icon5)
        self.bt_min.setObjectName("bt_min")
        self.horizontalLayout_3.addWidget(self.bt_min)
        self.bt_minfullscreen = QtWidgets.QPushButton(parent=self.frame_5)
        self.bt_minfullscreen.setMinimumSize(QtCore.QSize(35, 35))
        self.bt_minfullscreen.setMaximumSize(QtCore.QSize(35, 35))
        self.bt_minfullscreen.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000000ff;\n"
            "border-radius:20px\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(170, 170, 255);\n"
            "border-radius:20px\n"
            "}")
        self.bt_minfullscreen.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/Full_Screen.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_minfullscreen.setIcon(icon6)
        self.bt_minfullscreen.setObjectName("bt_minfullscreen")
        self.horizontalLayout_3.addWidget(self.bt_minfullscreen)
        self.bt_maxfullscreen = QtWidgets.QPushButton(parent=self.frame_5)
        self.bt_maxfullscreen.setMinimumSize(QtCore.QSize(35, 35))
        self.bt_maxfullscreen.setMaximumSize(QtCore.QSize(35, 35))
        self.bt_maxfullscreen.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000000ff;\n"
            "border-radius:20px\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(170, 170, 255);\n"
            "border-radius:20px\n"
            "}")
        self.bt_maxfullscreen.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/Exit_Full_Screen.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_maxfullscreen.setIcon(icon7)
        self.bt_maxfullscreen.setObjectName("bt_maxfullscreen")
        self.horizontalLayout_3.addWidget(self.bt_maxfullscreen)
        self.bt_exit = QtWidgets.QPushButton(parent=self.frame_5)
        self.bt_exit.setMinimumSize(QtCore.QSize(35, 35))
        self.bt_exit.setMaximumSize(QtCore.QSize(35, 35))
        self.bt_exit.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000000ff;\n"
            "border-radius:20px\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(255, 0, 0);\n"
            "border-radius:20px\n"
            "}")
        self.bt_exit.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Images/Exit.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_exit.setIcon(icon8)
        self.bt_exit.setObjectName("bt_exit")
        self.horizontalLayout_3.addWidget(self.bt_exit)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.page1)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.layout_comics = QtWidgets.QGridLayout()
        self.layout_comics.setSpacing(0)
        self.layout_comics.setObjectName("layout_comics")
        self.gridLayout_3.addLayout(self.layout_comics, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.layout_personajes = QtWidgets.QGridLayout()
        self.layout_personajes.setSpacing(50)
        self.layout_personajes.setObjectName("layout_personajes")
        self.gridLayout_5.addLayout(self.layout_personajes, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page4.setObjectName("page4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page4)
        self.verticalLayout_4.setContentsMargins(200, 0, 200, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.page4)
        self.label_4.setMinimumSize(QtCore.QSize(300, 60))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Images/creators.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.page4)
        self.label_5.setMinimumSize(QtCore.QSize(200, 200))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Images/participantes.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.gif = QtWidgets.QLabel(parent=self.page4)
        self.gif.setMinimumSize(QtCore.QSize(500, 15))
        self.gif.setMaximumSize(QtCore.QSize(16777215, 200))
        self.gif.setText("")
        self.gif.setScaledContents(True)
        self.gif.setObjectName("gif")
        self.verticalLayout_4.addWidget(self.gif)
        self.stackedWidget.addWidget(self.page4)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
