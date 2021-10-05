from abc import ABC, abstractmethod


class Position(metaclass=ABC):
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

    @abstractmethod
    def set_pos(self):
        pass
