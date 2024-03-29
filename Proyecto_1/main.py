import sys
import requests

from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWidgets, QtGui
from interfaz import Ui_MainWindow
from personajes_url import Personajes_Url
from descripcion_personajes import DescripcionPersonajes
from comics_url import Comics_url
from descripcion_comics import DescripcionComics
from PyQt6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.interfaz = Ui_MainWindow()  # Se carga la interfaz
        self.interfaz.setupUi(self)

        self.vacia = []

        self.cont = 0
        self.contc = 0

        self.descripcionpersonaje = DescripcionPersonajes()
        self.descripcioncomics = DescripcionComics()

        self.button_name = []
        self.button_namec = []

        info_personajes = Personajes_Url().personajes
        self.personajes = info_personajes['data']['results']
        self.imagen_personaje = []
        self.nombre_personaje = []
        self.desc_personaje = []

        info_comics = Comics_url().comics
        self.comics = info_comics['data']['results']
        self.imagen_comics = []
        self.nombre_comic = []
        self.desc_comics = []
        self.personajes_existentes = []
        self.creadores_nombre = []
        self.creadores_imagen = []

        self.pixmap = QtGui.QPixmap()
        self.pixmapc = QtGui.QPixmap()
        self.pixmapcreadores = QtGui.QPixmap()
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
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

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
        self.comics_present()

        x = 0
        xc = 0
        for cont in range(10):
            self.personaje_presentacion(x)
            self.button_name[x].clicked.connect(self.connect_bt_personajes)
            x += 1

        for contc in range(10):
            self.comics_presentacion(xc)
            self.button_namec[xc].clicked.connect(self.connect_bt_comics)
            xc += 1
        self.descripcionpersonaje.setLayout(self.descripcionpersonaje.layoutmain)

        self.descripcioncomics.setLayout(self.descripcioncomics.layoutmain)

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
        for columnas in range(2):
            for filas in range(5):
                for caracter in range(10):
                    image_data = requests.get(self.personajes[self.cont]['thumbnail']['path']+'.jpg').content
                    name = self.personajes[self.cont]['name']

                    self.button_name.insert(self.cont, QtWidgets.QPushButton(name))

                    self.pixmap.loadFromData(image_data)

                    label_nombre = QtWidgets.QLabel(name)
                    label_image = QtWidgets.QLabel()
                    label_image.setPixmap(self.pixmap)
                    label_image.setFixedWidth(160)
                    label_image.setFixedHeight(160)
                    label_image.setScaledContents(True)

                    completed = QtWidgets.QVBoxLayout()
                    completed.addWidget(label_image)
                    completed.addWidget(label_nombre)
                    completed.addWidget(self.button_name[self.cont])

                    self.interfaz.layout_personajes.addLayout(completed, columnas, filas)

                self.cont += 1

        self.interfaz.page3.setLayout(self.interfaz.layout_personajes)

    # Pagina personajes
    def comics_present(self):
        for columnas in range(2):
            for filas in range(5):
                for comic in range(10):
                    image_data = requests.get(self.comics[self.contc]['thumbnail']['path'] + '.jpg').content
                    title = self.comics[self.contc]['title']
                    date = self.comics[self.contc]['dates'][0]['date']
                    self.button_namec.insert(self.contc, QtWidgets.QPushButton(title))

                    self.pixmapc.loadFromData(image_data)

                    label_imagec = QtWidgets.QLabel()
                    label_imagec.setPixmap(self.pixmapc)
                    label_imagec.setFixedWidth(160)
                    label_imagec.setFixedHeight(160)
                    label_imagec.setScaledContents(True)
                    label_nombrec = QtWidgets.QLabel(title)
                    label_fechac = QtWidgets.QLabel(date)

                    completedc = QtWidgets.QVBoxLayout()

                    completedc.addWidget(label_imagec)
                    completedc.addWidget(label_nombrec)
                    completedc.addWidget(label_fechac)
                    completedc.addWidget(self.button_namec[self.contc])

                    self.interfaz.layout_comics.addLayout(completedc, columnas, filas)

                self.contc += 1

        self.interfaz.page2.setLayout(self.interfaz.layout_comics)

    # Pagina info
    def info(self):
        self.gif()

    def personaje_presentacion(self, x):
        self.imagen_personaje.insert(x, requests.get(self.personajes[x]['thumbnail']['path'] + '.jpg').content)
        self.nombre_personaje.insert(x, self.personajes[x]['name'])
        self.desc_personaje.insert(x, self.personajes[x]['description'])

        self.pixmap.loadFromData(self.imagen_personaje[x])

        self.descripcionpersonaje.image.setPixmap(self.pixmap)
        self.descripcionpersonaje.image.setFixedWidth(160)
        self.descripcionpersonaje.image.setFixedHeight(160)
        self.descripcionpersonaje.image.setScaledContents(True)
        self.descripcionpersonaje.nombre.setText(self.nombre_personaje[x])
        self.descripcionpersonaje.descripcion.setText(self.desc_personaje[x])

    def connect_bt_personajes(self):
        self.descripcionpersonaje.layoutmain.addWidget(self.descripcionpersonaje.image)
        self.descripcionpersonaje.layoutmain.addWidget(self.descripcionpersonaje.nombre)
        self.descripcionpersonaje.layoutmain.addWidget(self.descripcionpersonaje.descripcion)

        self.descripcionpersonaje.exec()

    def comics_presentacion(self, xc):
        self.imagen_comics.insert(xc, requests.get(self.comics[xc]['thumbnail']['path'] + '.jpg').content)
        self.nombre_comic.insert(xc, self.comics[xc]['title'])
        self.desc_comics.insert(xc, self.comics[xc]['description'])

        if self.comics[xc]['characters']['items'] == self.vacia:
            self.personajes_existentes.insert(xc, '')
        else:
            self.personajes_existentes.insert(xc, self.comics[xc]['characters']['items'][0]['name'])

        if self.comics[xc]['creators']['items'] == self.vacia:
            self.creadores_nombre.insert(xc, '')
        else:
            self.creadores_nombre.insert(xc, self.comics[xc]['creators']['items'][0]['name'])

        url_image_creators = (self.comics[xc]['creators']['items'])
        tamanio_creators = (self.comics[xc]['creators']['available'])
        listimage = []
        labels = []
        if tamanio_creators > 1:
            for c in range(tamanio_creators):
                listimage.insert(c, requests.get(
                    url_image_creators[0]['resourceURI'] +
                    '?ts=1&apikey=130c7354b5734b793a253f9087d61518&hash=a165aa46a0c484d5a49298745951c610').json())
                self.creadores_imagen.insert(
                    xc, requests.get(listimage[c]['data']['results'][0]['thumbnail']['path'] + '.jpg').content)

                image = QtWidgets.QHBoxLayout()
                labels.insert(c, QtWidgets.QLabel())
                image.addWidget(labels[c])

                self.pixmapcreadores.loadFromData(self.creadores_imagen[xc])
                self.descripcioncomics.creadores_foto.setPixmap(self.pixmapcreadores)
                self.descripcioncomics.creadores_foto.setPixmap(self.pixmapcreadores)
                self.descripcioncomics.creadores_foto.setFixedWidth(100)
                self.descripcioncomics.creadores_foto.setFixedHeight(160)
                self.descripcioncomics.creadores_foto.setScaledContents(True)

        elif tamanio_creators == 0:
            self.creadores_imagen.insert(xc, '')

        else:
            image = requests.get(
                url_image_creators[0]['resourceURI'] +
                '?ts=1&apikey=130c7354b5734b793a253f9087d61518&hash=a165aa46a0c484d5a49298745951c610').json()
            self.creadores_imagen.insert(xc, requests.get(
                image['data']['results'][0]['thumbnail']['path'] + '.jpg').content)
            self.pixmapcreadores.loadFromData(self.creadores_imagen[xc])
            self.descripcioncomics.creadores_foto.setPixmap(self.pixmapcreadores)
            self.descripcioncomics.creadores_foto.setFixedWidth(100)
            self.descripcioncomics.creadores_foto.setFixedHeight(160)
            self.descripcioncomics.creadores_foto.setScaledContents(True)

        self.pixmapc.loadFromData(self.imagen_comics[xc])

        self.descripcioncomics.image.setPixmap(self.pixmapc)
        self.descripcioncomics.image.setFixedWidth(160)
        self.descripcioncomics.image.setFixedHeight(160)
        self.descripcioncomics.image.setScaledContents(True)
        self.descripcioncomics.nombre.setText(self.nombre_comic[xc])
        self.descripcioncomics.descripcion.setText(self.desc_comics[xc])
        self.descripcioncomics.personajes.setText(self.personajes_existentes[xc])
        self.descripcioncomics.creadores.setText(self.creadores_nombre[xc])

    def connect_bt_comics(self):
        self.descripcioncomics.layoutmain.addWidget(self.descripcioncomics.image)
        self.descripcioncomics.layoutmain.addWidget(self.descripcioncomics.nombre)
        self.descripcioncomics.layoutmain.addWidget(self.descripcioncomics.descripcion)
        self.descripcioncomics.layoutmain.addWidget(self.descripcioncomics.personajes)
        self.descripcioncomics.layoutmain.addWidget(self.descripcioncomics.creadores)
        self.descripcioncomics.layoutmain.addWidget(self.descripcioncomics.creadores_foto)

        self.descripcioncomics.exec()


app = QApplication(sys.argv)
mi_app = VentanaPrincipal()
mi_app.show()
app.exec()
