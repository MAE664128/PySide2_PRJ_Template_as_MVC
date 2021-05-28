from typing import Optional, Union, Dict

from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QObject
from .ui_main import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model: Union[QObject, Dict[QObject]], main_controller: QObject, title_win: Optional[str]):
        super().__init__()

        self.__model = model
        self.__main_controller = main_controller
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        if title_win is not None:
            self.setWindowTitle(title_win)

        # подключить виджеты к контроллеру
        self.__ui.line_home_family.textChanged.connect(self.__main_controller.change_line_home_family)
        self.__ui.line_home_name.textChanged.connect(self.__main_controller.change_line_home_name)
        self.__ui.line_home_middle_name.textChanged.connect(self.__main_controller.change_line_home_middle_name)

        self.__ui.bn_home_clear.clicked.connect(self.__main_controller.clear)

        # Прослушиваем сигналы от модели
        self.__model.line_family_changed.connect(self.on_line_family_changed)
        self.__model.line_name_changed.connect(self.on_line_name_changed)
        self.__model.line_middle_name_changed.connect(self.on_line_middle_name_changed)

        # устанавливаем значение по умолчанию
        self.__main_controller.change_line_home_family("")
        self.__main_controller.change_line_home_name("")
        self.__main_controller.change_line_home_middle_name("")

    @Slot(str)
    def on_line_family_changed(self, value):
        self.__ui.line_home_family.setText(value)

    @Slot(str)
    def on_line_name_changed(self, value):
        self.__ui.line_home_name.setText(value)

    @Slot(str)
    def on_line_middle_name_changed(self, value):
        self.__ui.line_home_middle_name.setText(value)
