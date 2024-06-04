from PyQt6.QtWidgets import (QWidget, QPushButton,
                             QLabel, QVBoxLayout,
                             QHBoxLayout, QLineEdit)


class Main_menu(QWidget):
    def __init__(self):
        super().__init__()  # Вызываю конструктор родительского класса QWidget
        self.main_layout_v = QVBoxLayout(self)

        self.label = QLabel()
        self.label.setText("ОИБ лаб.4 - автор Пихуров Матвей 6211-100503D")
        self.label.setStyleSheet("font-size: 18px;")

        self.label_for_path = QLabel()
        self.label_for_path.setText("Введите данные для поиска карты:")
        self.label_for_path.setStyleSheet("font-size: 12px; margin-top: 15px")

        self.horizontal_layout_for_path = QHBoxLayout()

        self.input_total_numbers = QLineEdit()
        self.input_total_numbers.setPlaceholderText("Введите кол-во цифр карты")
        self.input_hash = QLineEdit()
        self.input_hash.setPlaceholderText("Введите хэш")
        self.input_last_number = QLineEdit()
        self.input_last_number.setPlaceholderText("Последние цифры")

        self.button_for_find_a_card = QPushButton()
        self.button_for_find_a_card.setText("Найти номер карты")
        self.button_for_find_a_card.setMinimumSize(50, 30)
        self.button_for_find_a_card.setStyleSheet("margin: 0 auto; padding: 5px")

        self.horizontal_layout_for_path.addWidget(self.input_total_numbers)
        self.horizontal_layout_for_path.addWidget(self.input_hash)
        self.horizontal_layout_for_path.addWidget(self.input_last_number)
        self.horizontal_layout_for_path.addWidget(self.button_for_find_a_card)

        self.label_for_found_card = QLabel()

        self.horizontal_layout_for_plot = QHBoxLayout()

        self.label_create_plot = QLabel()
        self.label_create_plot.setText("Создать график зависимости времени поиска от ядер процессора:")
        self.label_create_plot.setStyleSheet("font-size: 12px")

        self.button_for_create_plot = QPushButton()
        self.button_for_create_plot.setText("Создать график")
        self.button_for_create_plot.setStyleSheet("margin: 0 auto; padding: 5px")

        self.horizontal_layout_for_plot.addWidget(self.label_create_plot)
        self.horizontal_layout_for_plot.addWidget(self.button_for_create_plot)

        self.label_check_algorithm_luna = QLabel()

        self.button_check_algorithm_luna = QPushButton()
        self.button_check_algorithm_luna.setText("Проверить последовательность алгоритмом Луна")
        self.button_check_algorithm_luna.setStyleSheet("margin: 15px auto 0 auto; padding: 0 5px")

        self.main_layout_v.addWidget(self.label)
        self.main_layout_v.addWidget(self.label_for_path)
        self.main_layout_v.addLayout(self.horizontal_layout_for_path)
        self.main_layout_v.addWidget(self.label_for_found_card)
        self.main_layout_v.addLayout(self.horizontal_layout_for_plot)
        self.main_layout_v.addWidget(self.label_check_algorithm_luna)
        self.main_layout_v.addWidget(self.button_check_algorithm_luna)
