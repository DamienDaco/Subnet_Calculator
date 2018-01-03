try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    print("[-] Import failed. PyQt5 library not found. \nTry installing it with: apt install python3-qt5")
    exit()
from ui.design_subnet_calculator import Ui_MainWindow
from app.logic import *
import sys

# TODO : Fix the user input box triggering multiple times
# TODO : Add feature to save ip list as .txt
# TODO : Add multithreading. App is freezing when displaying large ranges


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.logic = Logic()

        self.box_user_input.editingFinished.connect(self.process_ip)

    def process_ip(self):

        if self.box_user_input.text():
            self.logic.ip = self.box_user_input.text()
            print('Current ip %s' % self.logic.ip)
            self.logic.ipv4_subnet_calc()

            if '/' in self.box_user_input.text():
                self.box_subnet_id.setText(self.logic.subnet_id)
                self.box_first_ip.setText(self.logic.first_ip)
                self.box_last_ip.setText(self.logic.last_ip)
                self.box_broadcast_ip.setText(self.logic.broadcast_ip)

                self.box_subnet_id_binary.setText(self.logic.string_subnet)
                self.box_first_ip_binary.setText(self.logic.string_first_ip)
                self.box_last_ip_binary.setText(self.logic.string_last_ip)
                self.box_broadcast_ip_binary.setText(self.logic.string_broadcast)

                self.logic.ip_range()
                for i in self.logic.ip_list:
                    self.text_browser.append(i)

        else:
            pass


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())