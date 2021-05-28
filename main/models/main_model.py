from PySide2.QtCore import QObject, Signal


class MainModel(QObject):
    line_family_changed = Signal(str)
    line_name_changed = Signal(str)
    line_middle_name_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.__family = ''
        self.__name = ''
        self.__middle_name = ''

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        self.__family = value
        self.line_family_changed.emit(value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        self.line_name_changed.emit(value)

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = value
        self.line_middle_name_changed.emit(value)
