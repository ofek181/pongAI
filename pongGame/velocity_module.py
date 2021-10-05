from abc import ABC, abstractmethod


class Velocity(ABC):
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
        __init__(self, x_vel, y_vel):
            Constructs all the necessary attributes for the Velocity object.
        set_vel(self):
            abstract method for setting the velocity.
    """

    def __init__(self, x_vel: float = 10, y_vel: float = 0):
        """
            Constructs all the necessary attributes for the Velocity object.
        """
        self.x_vel = x_vel
        self.y_vel = y_vel

    @abstractmethod
    def _set_velocity(self, x_vel: float, y_vel: float):
        """
            Abstract method for setting velocity to later be implemented.
        """
        pass
