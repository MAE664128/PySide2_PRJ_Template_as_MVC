import datetime
from time import sleep

from PySide2.QtCore import QObject, Signal, QThread


class Clocker(QObject):
    """ Часы """
    datetime_text = Signal(str)
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.datetime_text.emit(datetime.datetime.now().strftime("%m.%d.%Y, %H:%M:%S"))
            sleep(1)
        self.finished.emit()

    def stop(self):
        self._isRunning = False


class MainModel(QObject):
    line_family_changed = Signal(str)
    line_name_changed = Signal(str)
    line_middle_name_changed = Signal(str)
    title_window_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.__family = ''
        self.__name = ''
        self.__middle_name = ''
        self.__title_window = ''
        self.create_and_run_tread()

    def create_and_run_tread(self):
        self.thread_connect_checker = QThread(parent=self)
        self.clocker = Clocker()
        self.clocker.moveToThread(self.thread_connect_checker)
        self.clocker.datetime_text.connect(self.update_title_window)
        self.thread_connect_checker.started.connect(self.clocker.run)
        self.thread_connect_checker.start()

    def update_title_window(self, value: str):
        self.title_window = str(value)
        self.title_window = str(value)

    @property
    def title_window(self):
        return self.__title_window

    @title_window.setter
    def title_window(self, value):
        self.__title_window = value
        self.title_window_changed.emit(value)

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
