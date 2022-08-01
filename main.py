from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 532)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # прозрачный фон
        self.setStyleSheet("background:transparent;")  # Прозрачный фон

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.label.setFont(font)  # дизайн лейбла
        self.label.setStyleSheet("color:rgb(255, 85, 0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText("00:00:00")


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QtCore.QTimer(self)  # добавление таймера

        self.timer.setInterval(100)

        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.label.setText(QtCore.QTime.currentTime().toString('hh:mm:ss'))  # +++
        self.label.style()
        self.label.adjustSize()

    def move2RightBottomCorner(win):  # вычисление расположения окна для правого нижнего края
        screen_geometry = QApplication.desktop().availableGeometry()
        screen_size = (screen_geometry.width(), screen_geometry.height())
        win_size = (win.frameSize().width(), win.frameSize().height())
        x = screen_size[0] - win_size[0]
        y = screen_size[1] - win_size[1] - 40
        win.move(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    app.setWindowIcon(QtGui.QIcon('Rick.png'))

    window.move(window.width() * -3, 0)  # убрать мерцание при перемещении окна

    window.setFixedWidth(300)  # фиксированный размер окна
    window.setFixedHeight(150)

    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # убираем шапку
    window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # окно поверх других окон
    window.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))

    window.show()
    ExampleApp.move2RightBottomCorner(window)
    app.exec_()
