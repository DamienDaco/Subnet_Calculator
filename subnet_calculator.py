try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *

except:
    print("[-] Import failed. PyQt5 library not found. \nTry installing it with: apt install python3-qt5")
    exit()
from ui.design_subnet_calculator import Ui_MainWindow
from app.logic import *
import sys

# TODO : Add multithreading. App is freezing when displaying large ranges


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.logic = Logic()
        self.file_name = None

        self.shortcut_enter = QShortcut(QKeySequence("Enter"), self)
        self.shortcut_enter.activated.connect(self.process_ip)
        self.action_save_as.triggered.connect(self.save_file)
        self.range_button.clicked.connect(self.display_ip_range)

    def process_ip(self):

        if self.box_user_input.text():
            self.logic.ip = self.box_user_input.text()
            print('Current ip %s' % self.logic.ip)
            self.logic.ipv4_subnet_calc_with_int()

            if '/' in self.box_user_input.text():

                if self.logic.host_bits > 1:

                    self.box_subnet_id.setText(self.logic.subnet_id)
                    self.box_first_ip.setText(self.logic.first_ip)
                    self.box_last_ip.setText(self.logic.last_ip)
                    self.box_broadcast_ip.setText(self.logic.broadcast_ip)

                    self.box_subnet_id_binary.setText(self.logic.binary_string_subnet_id)
                    self.box_first_ip_binary.setText(self.logic.binary_string_first_ip)
                    self.box_last_ip_binary.setText(self.logic.binary_string_last_ip)
                    self.box_broadcast_ip_binary.setText(self.logic.binary_string_broadcast)

                if self.logic.host_bits == 1:

                    self.box_first_ip.setText(self.logic.first_ip)
                    self.box_last_ip.setText(self.logic.last_ip)
                    self.box_subnet_id.clear()
                    self.box_broadcast_ip.clear()
                    self.box_subnet_id_binary.clear()
                    self.box_broadcast_ip_binary.clear()

                    self.box_first_ip_binary.setText(self.logic.binary_string_first_ip)
                    self.box_last_ip_binary.setText(self.logic.binary_string_last_ip)

                if self.logic.host_bits == 0:

                    self.box_first_ip.setText(self.logic.first_ip)

                    self.box_last_ip.clear()
                    self.box_subnet_id.clear()
                    self.box_broadcast_ip.clear()
                    self.box_last_ip_binary.clear()
                    self.box_subnet_id_binary.clear()
                    self.box_broadcast_ip_binary.clear()

                    self.box_first_ip_binary.setText(self.logic.binary_string_first_ip)

        else:
            pass

    def display_ip_range(self):

        self.process_ip()
        self.logic.start_thread()
        self.logic.thread.worker.str_signal.connect(self.append_to_txt_browser)

    def append_to_txt_browser(self, s):
        self.text_browser.setText(s)

    def save_file(self):

        if self.file_name is None:                                                   # Check if file name exists, if not, open save dialog
            self.file_name = QFileDialog.getSaveFileName(self, 'Save File ', '.')[0] # This function returns a tuple, so let's extract the file path with [0]

        if not self.file_name.endswith('.txt'):                                      # If no extension specified, add .txt
            self.file_name += '.txt'

        with open(self.file_name, 'a') as file:
            for i in self.logic.ip_list:
                file.write('%s\n' % i)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())