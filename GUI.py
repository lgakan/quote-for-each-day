from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
import winsound
import time
import datetime
import json
import codecs
from time_functions import data_years, data_months, data_h, data_min, path_time_next, data_sek, data_day

sys.stdout.encoding == 'cp852'

path_time_in_app = "Time_in_app.txt"
path_aphorism = "json"
path_index = "index.txt"

# Aphorism getting
with open(path_aphorism) as json_file:
    data = json.load(json_file)


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(580, 300, 700, 500)
        self.setWindowTitle(" Afed ")
        self.initUI()
        # blocked resize
        self.setFixedSize(825, 613)

    def initUI(self):
        layout = QVBoxLayout()

        # Greeting at the top
        self.Welcome = QtWidgets.QLabel(self)
        self.Welcome.setGeometry(330, 0, 131, 41)
        self.Welcome.setText("Welcome our guest!")

        # aphorism
        self.aphorism = QtWidgets.QLabel(self)
        self.aphorism.setGeometry(330, 180, 131, 41)

        # author
        self.author = QtWidgets.QLabel(self)
        self.author.setGeometry(330, 230, 47, 13)

        # label connected to time to next aphorism
        self.time_to_next = QtWidgets.QLabel(self)
        self.time_to_next.setGeometry(330, 260, 47, 13)

        # Adding aphorism button
        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(300, 40, 150, 25)
        self.button.setText("Get Your Aphorism!")
        self.button.clicked.connect(self.press)

        # Clock
        fnt = QFont('Open Sans', 12, QFont.Bold)

        self.clock = QtWidgets.QLabel(self)
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setGeometry(750, 580, 80, 40)
        self.clock.setFont(fnt)

        layout.addWidget(self.clock)
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)
        self.show_time()

    # CLock functionality
    # Checking if 24h passed, showing right aphorism with music

    def press(self):
        # Getting last date
        with open(path_time_next, 'r') as f:
            previous_date = f.read()

        # Converting time into string type
        current_data = datetime.datetime.now()
        current_data = str(current_data)

        previous_date_to_compare = map(lambda x: x, previous_date)
        current_data_to_compare = map(lambda x: x, current_data)

        previous_date_to_compare = list(previous_date_to_compare)
        current_data_to_compare = list(current_data_to_compare)

        previous_year = data_years(previous_date_to_compare)
        curr_year = data_years(current_data_to_compare)

        previous_month = data_months(previous_date_to_compare)
        curr_month = data_months(current_data_to_compare)

        previous_day = data_day(previous_date_to_compare)
        curr_day = data_day(current_data_to_compare)

        previous_h = data_h(previous_date_to_compare)
        curr_h = data_h(current_data_to_compare)

        previous_min = data_min(previous_date_to_compare)
        curr_min = data_min(current_data_to_compare)

        previous_sek = data_sek(previous_date_to_compare)
        curr_sek = data_sek(current_data_to_compare)
        # --------------------------------------------------------------------------------------

        # Showing right aphorism

        if (curr_year >= previous_year):
            if (curr_month >= previous_month):
                if (curr_day >= (previous_day + 1)):
                    if (curr_h >= previous_h):
                        if (curr_min >= previous_min):
                            if (curr_sek >= previous_sek):
                                # Getting right aphorism's index from file
                                with open(path_index, 'r') as f:
                                    index = int(f.read())
                                # Showing aphorism code
                                self.author.setText(data['id'][index]['autor'])
                                self.aphorism.setText(data['id'][index]['aforyzm'])
                                self.time_to_next.setText("TUTAJ BD CZAS")
                                self.update_size()
                                # Music
                                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                                # Ensuring compliance of indexes
                                if (index > 99):
                                    index = 0
                                else:
                                    index = index + 1
                                # Saving new indexes into file
                                with open(path_index, 'w') as f:
                                    f.write(str(index))
                                # Saving new date into file
                                with open(path_time_next, 'w') as f:
                                    f.write(current_data)
                            else:
                                print("Nie minelo 24 h sekundy")
                        else:
                            print("Nie minelo 24 h min")
                    else:
                        print("Nie minelo 24 h  godziny")
                else:
                    print("Nie minelo 24 h  dni")
            else:
                print("Nie minelo 24 h miesiace")
        else:
            print("Nie minelo 24 h lata")

    # Writing size function
    def update_size(self):
        self.author.adjustSize()
        self.aphorism.adjustSize()
        self.time_to_next.adjustSize()

    # Clock function
    def show_time(self):
        current_time = QTime.currentTime()

        displayTxt = current_time.toString('hh:mm:ss')
        print(displayTxt)

        self.clock.setText(displayTxt)

    def closeEvent(self, event):
        # Window for confirm closing app
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirm Exit...",
                                                "Are you sure you want to exit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        event.ignore()
        # If we confirm app closing
        if result == QtWidgets.QMessageBox.Yes:
            # Downloading and saving moment of app closing
            end = time.time()
            # Translate total time in app from string type from path_time_in_app file into chars table
            in_file = open(path_time_in_app, 'r')
            lines = []
            for line in in_file:
                lines.append(line)
            in_file.close()
            previous = 0
            # Elements of table are projected onto floats. Next they are summed up
            for line in lines:
                number = float(line)
                previous = + number

            previous = previous / len(lines)
            # Total time in app
            current = int(previous + ((end - start) * 1))
            # Time is overwritten by new one
            with open(path_time_in_app, "w") as f:
                f.write(str(current))
                f.close()
            # app closing
            event.accept()





def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    # showing and closing window
    win.show()
    sys.exit(app.exec_())


start = time.time()
window()
