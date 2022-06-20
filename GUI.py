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

# pobranie z pliku tekstowego odpowedniego aforyzmu
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

        # Powitanie w na górze
        self.Welcome = QtWidgets.QLabel(self)
        self.Welcome.setGeometry(330, 0, 131, 41)
        self.Welcome.setText("Welcome our guest!")

        # aforyzm
        self.aphorism = QtWidgets.QLabel(self)
        self.aphorism.setGeometry(330, 180, 131, 41)

        # autor
        self.author = QtWidgets.QLabel(self)
        self.author.setGeometry(330, 230, 47, 13)

        # label od czasu do next aforyzmu
        self.time_to_next = QtWidgets.QLabel(self)
        self.time_to_next.setGeometry(330, 260, 47, 13)

        # Przycisk od dawania aforyzmu
        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(300, 40, 150, 25)
        self.button.setText("Get Your Aphorism!")
        self.button.clicked.connect(self.press)

        # zegar
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

    # Funkcja odnoszaca sie do przycisku
    # sprawdza czy minelo 24 h, wyswietla odpowiedni aforyzym i dodaje muzyczke

    def press(self):
        # z pliku pobiera ostatnia zapisana date
        with open(path_time_next, 'r') as f:
            previous_date = f.read()
        # program pobiera obecna date z komputera i zamieniamy typ na str
        current_data = datetime.datetime.now()
        current_data = str(current_data)
        # Dla obu dat korzystamy z map ()
        previous_date_to_compare = map(lambda x: x, previous_date)
        current_data_to_compare = map(lambda x: x, current_data)
        # z wczesniej uwtorzonych map() robimy listy charow
        previous_date_to_compare = list(previous_date_to_compare)
        current_data_to_compare = list(current_data_to_compare)
        # Przypisujemy do zmiennych poszczegolne czesci daty aby potem moc je porownac
        # ------------------------------------------------------------------------------------
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

        # Po sprawdzeniu czy minelo 24 h wyswietlanie odpowiedniego aforyzmu

        if (curr_year >= previous_year):
            if (curr_month >= previous_month):
                if (curr_day >= (previous_day + 1)):
                    if (curr_h >= previous_h):
                        if (curr_min >= previous_min):
                            if (curr_sek >= previous_sek):
                                # otwieranie pliku z zawartym ideksem danego aforyzmu do wyswietlenia
                                with open(path_index, 'r') as f:
                                    index = int(f.read())
                                # komendy odpoiwadajace za wyswietlanie aforyzmu
                                self.author.setText(data['id'][index]['autor'])
                                self.aphorism.setText(data['id'][index]['aforyzm'])
                                self.time_to_next.setText("TUTAJ BD CZAS")
                                self.update_size()
                                # muzyczka po kliknieciu przycisku
                                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                                # funkcja ktora zapewnia ze idex bedzie odpowiedni
                                if (index > 99):
                                    index = 0
                                else:
                                    index = index + 1
                                # zapisywanie nowego indexu do pliku
                                with open(path_index, 'w') as f:
                                    f.write(str(index))
                                # zapisanie nowej daty do pliku z racji ze warunek miniecia 24 zostal spelniony
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

    # dopasowywuje dlugosc aby caly napis sie wyswietlil
    def update_size(self):
        self.author.adjustSize()
        self.aphorism.adjustSize()
        self.time_to_next.adjustSize()

    # Funckja od zegara
    def show_time(self):
        current_time = QTime.currentTime()

        displayTxt = current_time.toString('hh:mm:ss')
        print(displayTxt)

        self.clock.setText(displayTxt)

    # liczenie całkowitego czasu w apce
    # okienko ktore pyta czy na pewno chcemy zamknac program
    # ---------------------------------------------------------------
    def closeEvent(self, event):
        # okienko od potwierdzenia zamkniecia
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirm Exit...",
                                                "Are you sure you want to exit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        event.ignore()
        # jesli potwierdzimy zamkniecie aplikacji ...
        if result == QtWidgets.QMessageBox.Yes:
            # pobieranie i zapisywanie do zmiennej "end" momentu zamknciecia aplikacji
            end = time.time()
            # Komendy ktore przeksztalcaja poprzedni cakowity czas w aplicaji [string] z pliku path_time_in_app na tablice [char]
            # ---------------------------------------------------------------------
            in_file = open(path_time_in_app, 'r')
            lines = []
            for line in in_file:
                lines.append(line)
            in_file.close()
            previous = 0
            # tutaj elementy tablicy [stringi] sa rzutowane na floaty oraz zostaja sumowane
            for line in lines:
                number = float(line)
                previous = + number

            previous = previous / len(lines)
            # do zmiennej "current" zostaje przypisany calkowity czas w aplikacji
            current = int(previous + ((end - start) * 1))
            # W pliku tesktowym stary calkowity czas jest nadpisywany przez nowy calkowity
            with open(path_time_in_app, "w") as f:
                f.write(str(current))
                f.close()
            # zamkniecie aplikacji
            event.accept()


# ---------------------------------------------------------------


# Okno samo w sobie
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    # bezpieczne pokazywanie i zamykanie okna
    win.show()
    sys.exit(app.exec_())


# wywolywanie okna
start = time.time()
window()
