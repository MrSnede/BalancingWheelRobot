#!/usr/bin/env python3


# http://stackoverflow.com/questions/12459811/how-to-embed-matplotib-in-pyqt-for-dummies


# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui

# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

# Matplotlib Figure object
from collections import deque
from matplotlib.figure import Figure
import matplotlib.animation as animation
#import matplotlib.pyplot as plt


class PlotValueBuffer:

    def __init__(self, maxLen):        # todo: maxlen wird mehrfach gesetzt
        self.ax = deque([0.0]*maxLen)  # todo: besserer Name fuer ax + ay
        self.ay = deque([0.0]*maxLen)
        self.maxLen = maxLen

    def addToBuf(self, buf, val):
        if len(buf) < self.maxLen:
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)
        print(buf)

    def add(self, datastring):
        """wird aus BotControllGUI aufgreufen, sobald ein neues Messwertdopel
        von der seriellen Konsole gelesen wurde"""
        datastring = datastring.decode('utf-8').rstrip("\r\n")
        data = [float(val) for val in datastring.split()]
        assert(len(data) == 2)
        self.addToBuf(self.ax, data[0])
        self.addToBuf(self.ay, data[1])

    def update(self, frameNum, a0, a1):
        a0.set_data(range(self.maxLen), self.ax)
        a1.set_data(range(self.maxLen), self.ay)
        return a0
        # Uebergabewerte und Rueckgabe sind Vorgabe von Matplotlib


class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # setup Matplotlib Figure and Axis
        self.fig = Figure(facecolor='snow', edgecolor='white')
        self.fig.patch.set_alpha(0.0)
        self.fig.set_tight_layout(True)

        self.ax = self.fig.add_subplot(111)
        self.ax.grid(b=True, which='major', color='b', linewidth=1.5)
        self.ax.grid(b=True, which='minor', color='r', linewidth=0.5)
        self.ax.set_axisbelow(True)
        self.ax.set_ylim([-60, 60])
        self.ax.set_xlim([0, 1000])       # todo: maxlen wird mehrfach gesetzt
        self.ax.axhline(y=0, linewidth=1.5, color='k')

        self.ax.set_ylabel('Neigung °', fontsize=14,
                           fontweight='bold', color='b')
        self.line_Plot1, = self.ax.plot([], [], label='Neigung °',
                                          linewidth=1.0, linestyle="-")
        self.line_Plot2, = self.ax.plot([], [], label='PID Antwort',
                                          linewidth=1.0, linestyle="-")
        #self.anim = animation.FuncAnimation(self.fig, PlotValueBuffer.update,
                                     #fargs=(self.line_Plot1, self.line_Plot2),
                                     #interval=100)
                                     # Values < 30 will rise a Tkinter Error

        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        #self.toolbar = NavigationToolbar(self.FigureCanvas, self)


class MplWidget(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent=None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # create a Buffer                 # todo: maxlen wird mehrfach gesetzt
        self.valueBuffer = PlotValueBuffer(maxLen=1000)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        # set the layout to the vertical box
        self.setLayout(self.vbl)
