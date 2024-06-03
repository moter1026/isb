import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = None
        self.first_task_widget = None
        self.second_task_widget = None
        self.third_task_widget = None

        self.create_menu()

    def create_menu(self):
        self.init_menu_widget()
        self.setCentralWidget(self.menu)
        self.show()

    def init_menu_widget(self):
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())