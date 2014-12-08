#!/usr/bin/env python3


# Copyright (C) 2011 by Eka A. Kurniawan
# eka.a.kurniawan(ta)gmail(tod)com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


#Links:
# https://translate.google.com/translate?hl=de&sl=fr&tl=de&u=http%3A%2F%2F
#               www.mon-club-elec.fr%2Fpmwiki_mon_club_elec%2F
#               pmwiki.php%3Fn%3DMAIN.PYQTLAB
# http://johnnado.com/pyqt-qtest-example/
# https://www.rfc1149.net/blog/2013/03/05/
#               what-is-the-difference-between-devttyusbx-and-devttyacmx/
#  Unix LF
#  Win  CR LF
#  MAC  CR

#todo:

#  http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
#  Werte vom Bot plotten                                               Prio1
#  Initial Werte von Bot holen und gui einstellen (zB die Slider)      Prio2
#  Speichern einbauen fuer Log, Matplot und Settings
#  Aktuell veraendert sich der Wert einen Sliders nicht, Wenn der Wert per Textbefehl direkt beeinflusst wird
#  Freie Slider und Schalter ueber GUI konfigurierbar

#Done
#  nach python3 migrieren                                  -> V02 23.11.2014
#  oeffnen der seriellen Konsole unter Windows,            -> V02 30.11.2014
#     aktuell lassen sich keine Ports auswaehlen

# C.J. bitte testen
#in der eingabeaufforderung:     python -m serial.tools.list_ports
#
# auf Windows muss es wohl 'COM4' heissen.


# >LedBlinkTime=100<

import sys, serial, os, time
from PyQt4.QtGui import QApplication, QMainWindow, QTextCursor
from PyQt4.QtCore import QObject, SIGNAL, QThread
from mainWindow import Ui_MainWindow
#from mplwidget import MplWidget

baudRates = ['9600',
             '38400',
             '115200',
             '1200000']

serialPort = ['/dev/ttyACM0',
              '/dev/ttyACM1',
              '/dev/ttyACM2',
              '/dev/ttyACM3',
              'COM7',
              'COM11',
              'COM3',
              'COM4',
              'COM5',
              'COM6']

"""
Zukunft als INI Datei zum Speichern

VERSION = BotControlGUI_V03
serProtocolEol= '\r'
serProtocolHeader  = '>'
serProtocolTrennzeichen  = '='
serProtocolFooter  = '<'

ArduinoSendSpeed = '20' # setze Sendegeschwindigkeit in ms

pitchPid_P = '1.0' # Wird nach Start der seriellen Verbindung abgefragt
pitchPid_I = '1.0' # Wird nach Start der seriellen Verbindung abgefragt
pitchPid_D = '1.0' # Wird nach Start der seriellen Verbindung abgefragt
pitchStepperSpeed = '0'
pitchStepperAccel = '0'


rollPid_P = '1.0' # Wird nach Start der seriellen Verbindung abgefragt
rollPid_I = '1.0' # Wird nach Start der seriellen Verbindung abgefragt
rollPid_D = '1.0' # Wird nach Start der seriellen Verbindung abgefragt
rollServoSpeed = '0'
rollServoAccel = '0'
"""


class CMainWindow(QMainWindow):
    def __init__(self, *args):
        self.ser = None
        self.reader = CReader()
        self.writer = CWriter()

        QMainWindow.__init__(*(self, ) + args)
        self.ui = Ui_MainWindow()
        self.setup_ui()
        self.print_info("\n!! Nach dem Verbinden wird 9 Sekunden gewartet !!\n")
        self.print_info("Da Arduino Uno bei einem Verbindungsaufbau neu bootet")

    def setup_ui(self):
        self.ui.setup_ui(self)
        self.ui.baudRateComboBox.addItems(baudRates)
        self.refresh_ports()
        QObject.connect(self.ui.refreshPortsPushButton,
                        SIGNAL("clicked()"), self.refresh_ports)
        QObject.connect(self.ui.connectPushButton,
                        SIGNAL("clicked()"), self.connect)
        QObject.connect(self.ui.disconnectPushButton,
                        SIGNAL("clicked()"), self.disconnect)
        QObject.connect(self.ui.cmdLineEdit,
                        SIGNAL("returnPressed()"), self.process_LineEntryCmd)
        QObject.connect(self.ui.P_HSlider,
                        SIGNAL("sliderReleased()"), self.process_SliderCmd)

        QObject.connect(self.reader,
                        SIGNAL("newData(QString)"), self.update_log)
        QObject.connect(self.reader,
                        SIGNAL("error(QString)"), self.print_error)
        QObject.connect(self.writer,
                        SIGNAL("error(QString)"), self.print_error)

    def get_selected_port(self):
        self.print_info(self.ui.portsComboBox.currentText())
        return self.ui.portsComboBox.currentText()

    def get_selected_baud_rate(self):
        return self.ui.baudRateComboBox.currentText()

    def refresh_ports(self):
        print(os.name)  # posix oder nt
        self.ui.portsComboBox.clear()
        self.ui.portsComboBox.addItems(sorted(serialPort))

    def connect(self):
        self.disconnect()
        try:
            self.print_info("Connecting to %s with %s baud rate." %
                          (self.get_selected_port(),
                           self.get_selected_baud_rate()))
            self.ser = serial.Serial(str(self.get_selected_port()),
                                     int(self.get_selected_baud_rate()),
                                     xonxoff=True)
            time.sleep(9)
            # arduino Uno bootet nach einer neu aufgebauten Verbindung neu,
            # wir warten darauf
            # dabei gibt es keine zur Zeit Rueckmeldung

            self.ser.flush()
            self.start_reader(self.ser)
            self.print_info("Verbindung Erfolgreich.\n")
        except:
            self.ser = None
            self.print_error("\nVerbindung fehlgeschlagen!")
            self.print_info("\nIst der Aduino am richtigen Port angeschlossen?")

    def disconnect(self):
        self.stop_threads()
        if self.ser is None:
            return
        try:
            if self.ser.isOpen:
                self.ser.close()
                self.print_info("Disconnected successfully.")
        except:
            self.print_error("Failed to disconnect!")
        self.ser = None

    def start_reader(self, ser):
        self.reader.start(ser)

    def stop_threads(self):
        self.stop_reader()
        self.stop_writer()

    def stop_reader(self):
        if self.reader.isRunning():
            self.reader.terminate()

    def stop_writer(self):
        if self.writer.isRunning():
            self.writer.terminate()

    def print_info(self, text):
        self.ui.logPlainTextEdit.appendPlainText(text)
        self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

    def print_error(self, text):
        self.ui.logPlainTextEdit.appendPlainText(text)
        self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

    def print_cmd(self, text):
        self.ui.logPlainTextEdit.appendPlainText(text + '\n')
        self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

    def update_log(self, text):
        self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)
        self.ui.logPlainTextEdit.insertPlainText(text)
        self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

    def process_LineEntryCmd(self):
        cmd = self.ui.cmdLineEdit.text()
        self.print_cmd(cmd+'\n')
        self.writer.start(self.ser, cmd)
        self.ui.cmdLineEdit.clear()

    def process_SliderCmd(self):
        sliderValue = ">LedBlinkTime=" + str(self.ui.P_HSlider.value()) + "<"
        print(sliderValue)
        self.print_cmd(sliderValue)
        self.writer.start(self.ser, sliderValue)

    def process_Cmd(self):
        cmd = self.ui.cmdLineEdit.text()
        self.print_cmd(cmd)
        self.writer.start(self.ser, cmd)
        self.ui.cmdLineEdit.clear()

    def closeEvent(self, event):
        self.disconnect()


class CReader(QThread):
    def start(self, ser, priority=QThread.InheritPriority):
        self.ser = ser
        QThread.start(self, priority)

    def run(self):
        while True:
            data = self.ser.readline()
            #print(data)
            self.emit(SIGNAL("newData(QString)"), data.decode())


class CWriter(QThread):
    def start(self, ser, cmd="", priority=QThread.InheritPriority):
        self.ser = ser
        #print(self.ser)
        print(cmd)
        self.cmd = str(cmd)+"\r"
        QThread.start(self, priority)
        print(self.cmd)

    def run(self):
        try:
            print("try: " + self.cmd)
            self.ser.write(self.cmd.encode())  # string into raw bytes
        except:
            errMsg = "Writer thread is not runnig."
            self.emit(SIGNAL("error(QString)"), errMsg)

    def terminate(self):
        print("aus")
        self.wait()
        QThread.terminate(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = CMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
