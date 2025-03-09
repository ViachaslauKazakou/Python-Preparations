from PyQt5 import QtCore, QtGui, QtWidgets

BUTTON_CONFIGS = [
    ("otvet1", 50, 50, "Ч1"),
    ("otvet2", 50, 100, "М2"),
    ("otvet3", 180, 50, "Б2"),
    ("otvet4", 180, 100, "М3"),
    ("otvet5", 310, 50, "Б3"),
    ("otvet6", 310, 100, "Ч4"),
    ("otvet7", 440, 50, "Ч5"),
    ("otvet8", 440, 100, "М6"),
    ("otvet9", 570, 50, "Б6"),
    ("otvet10", 570, 100, "М7"),
    ("otvet11", 700, 50, "Б7"),
    ("otvet12", 700, 100, "Ч8"),
]


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 803)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create buttons and connect signals
        self.buttons = {}
        for name, x, y, text in BUTTON_CONFIGS:
            button = self.create_button(name, x, y)
            button.setText(text)
            button.clicked.connect(lambda checked, t=text: self.otvetu(t))
            self.buttons[name] = button

        # Create labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 690, 421, 61))
        self.label.setText("Пример текста в низу")
        self.label.setObjectName("label")

        self.primer = QtWidgets.QLabel(self.centralwidget)
        self.primer.setGeometry(QtCore.QRect(266, 390, 221, 41))
        self.primer.setText("Ч1")
        self.primer.setObjectName("primer")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def otvetu(self, otvet):
        """Handle button click and compare answers"""
        label_text = self.primer.text()  # Call the text() method
        print(f"Button text: {otvet}, Label text: {label_text}")
        print(f"Types - Button: {type(otvet)}, Label: {type(label_text)}")

        # Ensure exact string comparison
        if str(otvet).strip() == str(label_text).strip():
            self.label.setText("Правильно!")
        else:
            self.label.setText("Неправильно!")

    def create_button(self, name, x, y):
        """Helper method to create a button with given parameters"""
        button = QtWidgets.QPushButton(self.centralwidget)
        button.setGeometry(QtCore.QRect(x, y, 75, 23))
        button.setObjectName(name)
        setattr(self, name, button)  # Make button accessible as self.otvet1, etc.
        return button


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
