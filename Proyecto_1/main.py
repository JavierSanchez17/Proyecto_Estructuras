import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWidgets
from interfaz import Ui_MainWindow


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.interfaz = Ui_MainWindow()    # Se carga la interfaz
        self.interfaz.setupUi(self)

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

        # Mostrar gif
        self.gif()

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
        self.interfaz.gif.setMaximumSize(700, 160)
        self.interfaz.gif.setAlignment(Qt.AlignmentFlag.AlignCenter)
        animation.start()


app = QApplication(sys.argv)
mi_app = VentanaPrincipal()
mi_app.show()
app.exec()
