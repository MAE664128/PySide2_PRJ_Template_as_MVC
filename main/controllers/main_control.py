from PySide2.QtCore import QObject, Slot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self.__model = model

    @Slot(str)
    def change_line_home_family(self, value):
        self.__model.family = value

    @Slot(str)
    def change_line_home_name(self, value):
        self.__model.name = value

    @Slot(str)
    def change_line_home_middle_name(self, value):
        self.__model.middle_name = value

    def clear(self):
        self.change_line_home_family("")
        self.change_line_home_name("")
        self.change_line_home_middle_name("")
