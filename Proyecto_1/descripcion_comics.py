from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton


class DescripcionComics(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('Descripcion Comic')
        self.layoutmain = QVBoxLayout()
        self.image = QLabel()
        self.nombre = QLabel()
        self.descripcion = QLabel()
        self.personajes = QLabel()
        self.creadores = QLabel()
        self.creadores_foto = QLabel()
        self.buton = QPushButton()
