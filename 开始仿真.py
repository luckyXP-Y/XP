#coding:utf-8

# 导入必要的模块
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets,QtGui
import matplotlib.pyplot as plt
import numpy as np
import sys

class My_Main_window(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(My_Main_window,self).__init__(parent)
        self.setWindowTitle('太阳能电池仿真')
        # 重新调整大小
        self.resize(800, 659)
        # 添加菜单中的按钮
        self.menu = QtWidgets.QMenu("仿真")
        self.menu_action = QtWidgets.QAction("开始仿真",self.menu)
        self.menu.action = QtWidgets.QAction("打开文件",self.menu)
        self.menu.addAction(self.menu_action)
        self.menuBar().addMenu(self.menu)
        # 添加事件
        self.menu_action.triggered.connect(self.plot_opaque_cube1)
        self.setCentralWidget(QtWidgets.QWidget())

    # 绘图方法
    def plot_opaque_cube1(self):
        x, y, z = np.indices((8, 8, 8))
        # draw cuboids in the top left and bottom right corners, and a link between
        # them
        cube1 = (x < 8) & (y < 8) & (z >= 0)
        cube2 = (x < 8) & (y < 8) & (z >= 2)
        cube3 = (x < 8) & (y < 8) & (z >= 4)
        cube4 = (x < 8) & (y < 8) & (z >= 6)
        # combine the objects into a single boolean array
        voxels = cube1 | cube2 | cube3 | cube4
        # set the colors of each object
        colors = np.empty(voxels.shape, dtype=object)
        colors[cube1] = 'gray'
        colors[cube2] = 'red'
        colors[cube3] = 'yellow'
        colors[cube4] = 'gray'

        # and plot everything
        ax = plt.figure().add_subplot(projection='3d')
        ax.voxels(voxels, facecolors=colors, edgecolor='k')

        # Demo 3: text2D
        # Placement 0, 0 would be the bottom left, 1, 1 would be the top right.
        ax.text2D(0.05, 0.95, "solar", transform=ax.transAxes)

        # Tweaking display region and labels

        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_zlim(0, 8)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()
       
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_Main_window()
    main_window.show()
    app.exec()      
import matplotlib.pyplot as plt
import numpy as np

# prepare some coordinates
x, y, z = np.indices((8, 8, 8))
# draw cuboids in the top left and bottom right corners, and a link between
# them
cube1 = (x < 8) & (y < 8) & (z >= 0)
cube2 = (x < 8) & (y < 8) & (z >= 2)
cube3 = (x < 8) & (y < 8) & (z >= 4)
cube4 = (x < 8) & (y < 8) & (z >= 6)
# combine the objects into a single boolean array
voxels = cube1 | cube2 | cube3 | cube4
# set the colors of each object
colors = np.empty(voxels.shape, dtype=object)
colors[cube1] = 'gray'
colors[cube2] = 'red'
colors[cube3] = 'yellow'
colors[cube4] = 'gray'

# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')

# Demo 3: text2D
# Placement 0, 0 would be the bottom left, 1, 1 would be the top right.
ax.text2D(0.05, 0.95, "solar", transform=ax.transAxes)

# Tweaking display region and labels

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_zlim(0, 8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
