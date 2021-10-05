from abc import ABC, abstractmethod


class Velocity(metaclass=ABC):
    def __init__(self):
        self.x_vel = 0
        self.y_vel = 0

    @abstractmethod
    def set_vel(self):
        pass
