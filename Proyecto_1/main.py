import sys
import requests

from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWidgets, QtGui
from interfaz import Ui_MainWindow
from personajes_url import Personajes_Url


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.interfaz = Ui_MainWindow()  # Se carga la interfaz
        self.interfaz.setupUi(self)

        info_personajes = Personajes_Url().personajes
        self.personajes = info_personajes['data']['results']

        # Nombre de la ventana principal
        self.setWindowTitle('Mundo Comic')

        # Se oculta el boton minimizar
        self.interfaz.bt_minfullscreen.hide()

        # Botones para minimizar | maximizar | cerrar
        self.interfaz.bt_min.clicked.connect(self.minimizar)
        self.interfaz.bt_minfullscreen.clicked.connect(self.normal)
        self.interfaz.bt_maxfullscreen.clicked.connect(self.maximinizar)
        self.interfaz.bt_exit.clicked.connect(lambda: self.close())

        # Linea de codigo para ocultar la barra de titulo
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Al acercar a el margen de arriba maximiza la ventana
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Conectar botones a las paginas correspondientes
        self.interfaz.bt_inicio.clicked.connect(
            lambda: self.interfaz.stackedWidget.setCurrentWidget(self.interfaz.page1))
        self.interfaz.bt_comics.clicked.connect(
            lambda: self.interfaz.stackedWidget.setCurrentWidget(self.interfaz.page2))
        self.interfaz.bt_personajes.clicked.connect(
            lambda: self.interfaz.stackedWidget.setCurrentWidget(self.interfaz.page3))
        self.interfaz.bt_info.clicked.connect(
            lambda: self.interfaz.stackedWidget.setCurrentWidget(self.interfaz.page4))

        self.info()
        self.characters()

    # Metodos
    # Minimizar Ventana
    def minimizar(self):
        self.showMinimized()

    # Salir de pantalla completa
    def normal(self):
        self.showNormal()
        self.interfaz.bt_minfullscreen.hide()
        self.interfaz.bt_maxfullscreen.show()

    # Colocar pantalla completa
    def maximinizar(self):
        self.showMaximized()
        self.interfaz.bt_maxfullscreen.hide()
        self.interfaz.bt_minfullscreen.show()

    # Crear Gif de a pagina info
    def gif(self):
        animation = QMovie('Images/fondo_info.gif')
        self.interfaz.gif.setMovie(animation)
        animation.start()

    # Pagina comics
    def characters(self):
        cont = 0
        for columnas in range(4):
            for filas in range(5):
                for caracter in range(len(self.personajes)):
                    image_data = requests.get(self.personajes[cont]['thumbnail']['path']+'.jpg').content
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(image_data)
                    label = QtWidgets.QLabel()
                    label.setPixmap(pixmap)
                    label.setFixedWidth(160)
                    label.setFixedHeight(160)
                    label.setScaledContents(True)

                    self.interfaz.layout_personajes.addWidget(label, columnas, filas)

                cont += 1

        self.interfaz.page2.setLayout(self.interfaz.layout_personajes)

    # Pagina personajes
    def comics(self):
        pass

    # Pagina info
    def info(self):
        self.gif()


app = QApplication(sys.argv)
mi_app = VentanaPrincipal()
mi_app.show()
app.exec()
