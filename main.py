from random import randint
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QListWidget, QStackedWidget,
                             QHBoxLayout, QListWidgetItem, QPushButton, QLabel)
import speed_typing
import csv
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import csv

import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import matplotlib


class LeftTabWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(LeftTabWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # Left and right layout (one QListWidget on the left + QStackedWidget on the right)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # List on the left
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        # Cascading window on the right
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)

        self.initUi()

    def dosomething(self, event):
        sh = 0
        x_list = list(range(1, 11))
        y_list = []

        with open('graph_info.csv', newline='') as File:
            reader = csv.reader(File, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if row != '':
                    y_list.append(int(row[0]))
                    sh += 1
        print(y_list, " кук кук кук  ", x_list)
        plt.title("Статистика")
        plt.ylabel("сл/м")
        plt.xlabel("попытки")
        plt.bar(range(len(y_list)), y_list, label="участник")
        plt.legend()
        plt.show()

    def initUi(self):
        # Initialization interface
        # Switch the sequence number in QStackedWidget by the current item change of QListWidget
        self.listWidget.currentRowChanged.connect(
        self.stackedWidget.setCurrentIndex)
        # Remove the border
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # Hide scroll bar
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Here we use the general text with the icon mode (you can also use Icon mode, setViewMode directly)
        # for i in range(5):
        item = QListWidgetItem(
            QIcon('Ok.png'), str('Тест'), self.listWidget)
        # Set the default width and height of the item (only height is useful here)
        item.setSizeHint(QSize(16777215, 60))
        # Text centered
        item.setTextAlignment(Qt.AlignCenter)

        item = QListWidgetItem(
            QIcon('Ok.png'), str('Статистика'), self.listWidget)
        # Set the default width and height of the item (only height is useful here)
        item.setSizeHint(QSize(16777215, 60))
        # Text centered
        item.setTextAlignment(Qt.AlignCenter)

        item = QListWidgetItem(
            QIcon('Ok.png'), str('Тест(МОД)'), self.listWidget)
        # Set the default width and height of the item (only height is useful here)
        item.setSizeHint(QSize(16777215, 60))
        # Text centered
        item.setTextAlignment(Qt.AlignCenter)

        item = QListWidgetItem(
            QIcon('Ok.png'), str('Сотрудничество'), self.listWidget)
        # Set the default width and height of the item (only height is useful here)
        item.setSizeHint(QSize(16777215, 60))
        # Text centered
        item.setTextAlignment(Qt.AlignCenter)

        # item = QListWidgetItem(
        #     QIcon('Ok.png'), str('?'), self.listWidget)
        # # Set the default width and height of the item (only height is useful here)
        # item.setSizeHint(QSize(16777215, 60))
        # # Text centered
        # item.setTextAlignment(Qt.AlignCenter)

        # содержимое страниц
        # Simulate 5 right-side pages (it won't loop with the top)
        btn = QPushButton('Чтобы начать тест, нажми сюда', self)
        # btn.set.setAlignment(Qt.AlignCenter)

        btn.setStyleSheet('background: rgb(15, 86, 153); color: rgb(0, 0, 0); margin: 20px;')
        self.stackedWidget.addWidget(btn)
        btn.clicked.connect(self.btnrun)

        # x_list = list(range(1, 6))
        # y_list = [22, 17, 81, 41, 25]
        #
        # plt.title("Статистика")
        # plt.ylabel("сл/м")
        # plt.xlabel("попытки")
        # plt.bar(x_list, y_list, label="участник")
        # plt.legend()
        # plt.show()

        label1 = QLabel("график", self)
        label1.setAlignment(Qt.AlignCenter)

        # Set the background color of the label (randomly here)
        # Added a margin margin here (to easily distinguish between QStackedWidget and QLabel colors)
        label1.setStyleSheet('background: rgb(0, 0, 0);')
        self.stackedWidget.addWidget(label1)

        label2 = QLabel('тест МОД', self)
        label2.setAlignment(Qt.AlignCenter)
        # Set the background color of the label (randomly here)
        # Added a margin margin here (to easily distinguish between QStackedWidget and QLabel colors)
        label2.setStyleSheet('background: rgb(%d, %d, %d);' % (  # margin: 50px;
            randint(0, 255), randint(0, 255), randint(0, 255)))
        self.stackedWidget.addWidget(label2)

        label3 = QLabel('This is the page 4', self)
        label3.setAlignment(Qt.AlignCenter)
        # Set the background color of the label (randomly here)
        # Added a margin margin here (to easily distinguish between QStackedWidget and QLabel colors)
        label3.setStyleSheet('background: rgb(%d, %d, %d);' % (  # margin: 50px;
            randint(0, 255), randint(0, 255), randint(0, 255)))
        self.stackedWidget.addWidget(label3)

        label4 = QLabel('This is the page 5', self)
        label4.setAlignment(Qt.AlignCenter)
        # Set the background color of the label (randomly here)
        # Added a margin margin here (to easily distinguish between QStackedWidget and QLabel colors)
        label4.setStyleSheet('background: rgb(%d, %d, %d);' % (  # margin: 50px;
            randint(0, 255), randint(0, 255), randint(0, 255)))
        self.stackedWidget.addWidget(label4)
        self.stackedWidget.widget(1).mousePressEvent = self.dosomething

    def btnrun(self):
        print('Ok')
        speed_typing.run()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# def dosomething(self, event):
#     x_list = list(range(1, 6))
#     y_list = [22, 17, 81, 41, 25]
#
#     plt.title("Статистика")
#     plt.ylabel("сл/м")
#     plt.xlabel("попытки")
#     plt.bar(x_list, y_list, label="участник")
#     plt.legend()
#     plt.show()


# style sheet
Stylesheet = """
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: black;
}
QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}
HistoryPanel::item:hover {background: rgb(52, 52, 52);}
QStackedWidget {background: rgb(30, 30, 30);}
QLabel {color: white;}
"""

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    w = LeftTabWidget()
    w.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

    if event.type == QUIT:
        self.running = False
        # pygame.display.quit()
        pygame.display.update()
        print('Go')
        pygame.display.quit()
        clock.tick(60)

# print(y_list)