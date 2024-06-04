import sys
import multiprocessing as mp

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow
)

from qt_application.main_menu import Main_menu
from funcitons_for_selection import Check_number_of_card


class My_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bins = ["512347", "518365", "521155", "522477", "530114",
                     "542247", "543367", "543762", "548328", "548791"]
        self.menu = None
        self.create_menu()

    def _init_check_number_of_card(self) -> Check_number_of_card:
        data = {
            "total_numbers": self.menu.input_total_numbers.text(),
            "BIN_gazprombank_mastercard_debit": self.bins,
            "last_numbers": self.menu.input_last_number.text(),
            "hash": self.menu.input_hash.text(),
            "file_serialization": "../files/found number.txt"
        }
        return Check_number_of_card(data["hash"], data["last_numbers"],
                                    data["BIN_gazprombank_mastercard_debit"],
                                    data["file_serialization"], data["total_numbers"])

    def create_menu(self):
        self.menu = Main_menu()
        self.menu.button_for_find_a_card.clicked.connect(self.on_find_a_card)
        self.menu.button_for_create_plot.clicked.connect(self.on_create_plot)
        self.menu.button_check_algorithm_luna.clicked.connect(self.on_check_luna)

        self.setCentralWidget(self.menu)
        self.show()

    def on_find_a_card(self):
        number_card = self._init_check_number_of_card()

        cores = mp.cpu_count()
        # print(cores)
        find_card = number_card.find_number_of_card(cores)
        if find_card:
            self.menu.label_for_found_card.setText(find_card)
            self.menu.label_for_found_card.setStyleSheet("color: green")
            number_card.serialization_number(find_card)
        else:
            self.menu.label_for_found_card.setText("Номер карты не получилось подобрать")
            self.menu.label_for_found_card.setStyleSheet("color: red")

    def on_create_plot(self):
        number_card = self._init_check_number_of_card()
        number_card.create_plot()

    def on_check_luna(self):
        number_card = self._init_check_number_of_card()
        cores = mp.cpu_count()
        find_card = number_card.find_number_of_card(cores)
        result = number_card.check_luna(find_card)

        if result:
            self.menu.label_check_algorithm_luna.setText(str(result))
            self.menu.label_check_algorithm_luna.setStyleSheet("color: green; font-size: 18px;")
        else:
            self.menu.label_check_algorithm_luna.setText(str(result))
            self.menu.label_check_algorithm_luna.setStyleSheet("color: red; font-size: 18px;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = My_app()
    sys.exit(app.exec())
