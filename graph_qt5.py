import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import matplotlib

x_list = list(range(1, 6))
y_list = [22, 17, 81, 41, 25]

plt.title("Статистика")
plt.ylabel("сл/м")
plt.xlabel("попытки")
plt.bar(x_list, y_list, label="участник")
plt.legend()
plt.show()

# поменять цвет и вставить в проект
