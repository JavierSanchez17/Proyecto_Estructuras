from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton


class DescripcionPersonajes(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('Descripcion Personaje')
        self.layoutmain = QVBoxLayout()
        self.image = QLabel()
        self.nombre = QLabel()
        self.descripcion = QLabel()
        self.buton = QPushButton()
