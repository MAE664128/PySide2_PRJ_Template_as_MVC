from main.models import MainModel
from main.controllers import MainController
from main.views import MainView

import sys


from PySide2 import QtCore
from PySide2.QtWidgets import QApplication

#  Для Перевода

_tr = QtCore.QCoreApplication.translate


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = MainModel()
        self.main_controller = MainController(self.model)
        self.main_view1 = MainView(self.model, self.main_controller, title_win="1")
        self.main_view2 = MainView(self.model, self.main_controller, title_win="2")
        self.main_view1.show()
        self.main_view2.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
