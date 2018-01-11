from PyQt5.QtCore import *


class Worker(QObject):
    str_signal = pyqtSignal(str)

    def __init__(self, first_ip, last_ip):
        super().__init__()
        self.first_ip = first_ip
        self.last_ip = last_ip
        self.is_running = True
        thread = QThread.currentThread()
        print("My current thread is %s" % thread)

    def task(self):

        while self.is_running:
            for i in range(self.first_ip, self.last_ip + 1):
                ip = self.integer_to_decimal(i)
                self.str_signal.emit(ip)
            self.is_running = False

    def stop(self):

        self.is_running = False

    def integer_to_decimal(self, i):

        i = '{0:032b}'.format(i)
        decimal_ip = '.'.join(map(str, [int(i[:8], 2), int(i[8:16], 2), int(i[16:24], 2), int(i[24:32], 2)]))
        return decimal_ip


class MultiThreading(QThread):

    def __init__(self, first_ip, last_ip):
        super().__init__()

        self.first_ip = first_ip
        self.last_ip = last_ip
        self.threads = []

    def start_thread(self):

        self.worker = Worker(self.first_ip, self.last_ip)
        self.thread = QThread()
        self.threads.append((self.worker, self.thread))
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.task)
        self.thread.start()

    def stop_thread(self):

        if len(self.threads) > 0:                       # Check if there's something in the list
            print("Sending stop signal to thread")
            for worker, thread in self.threads:         # Let's go through the list of threads
                worker.stop()                           # And send the stop signal to each worker/thread
                thread.quit()
                thread.wait()

        self.threads = []                               # When done, reset list