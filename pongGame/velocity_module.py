from abc import ABC, abstractmethod


class Velocity(metaclass=ABC):
    """
        A class for implementing x,y velocity on the screen.
        ----------------------------
        Attributes
        ----------------------------
        x_vel
            x velocity on the screen.
        y_vel
            y velocity on the screen.
        ----------------------------
        Methods
        ----------------------------
        __init__(self):
            Constructs all the necessary attributes for the Velocity object.
        set_vel(self):
            abstract method for setting the velocity.
    """

    def __init__(self):
        """
            Constructs all the necessary attributes for the Velocity object.
        """
        self.x_vel = 0
        self.y_vel = 0

    @abstractmethod
    def set_vel(self):
        """
            Abstract method for setting velocity to later be implemented.
        """
        pass
