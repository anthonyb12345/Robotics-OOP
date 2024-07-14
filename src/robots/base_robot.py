from abc import ABC, abstractmethod
import time

class Robot(ABC):
    def __init__(self, name: str, battery_level: int, status: str) -> None:
        """
        Initialize a Robot object.

        Args:
            name (str): The name of the robot.
            battery_level (int): The initial battery level of the robot (0 to 100).
            status (str): The initial status of the robot ('idle', 'working', 'charging').

        Raises:
            ValueError: If name is not a string, battery_level is not an integer within [0, 100],
                        or status is not one of 'idle', 'working', 'charging'.
        """
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(battery_level, int) or not (0 <= battery_level <= 100):
            raise ValueError("battery_level must be an integer between 0 and 100")
        if status not in ['idle', 'working', 'charging']:
            raise ValueError("status must be one of: 'idle', 'working', 'charging'")

        self.name = name
        self.battery_level = battery_level
        self.status = status

    def charge(self) -> None:
        """
        Simulate charging the robot's battery to 100%.

        If the battery level is below 100%, it increases by 5% every second until it reaches 100%.

        Returns:
            None
        """
        self.status = 'charging'
        print(f"{self.name} is {self.status}")
        while self.battery_level < 100:
            if (self.battery_level + 5) > 100:
                self.battery_level = 100
            else:
                self.battery_level += 5
            time.sleep(1)

        self.status = 'idle'

    @abstractmethod
    def work(self) -> None:
        """
        Abstract method representing the work behavior of the robot.

        This method must be implemented in subclasses.
        """
        pass

    def report_status(self) -> None:
        """
        Print the current status of the robot.

        Returns:
            None
        """
        print(f"name= {self.name}, battery level= {self.battery_level}, status= {self.status}")

    def get_name(self) -> str:
        """
        Get the name of the robot.

        Returns:
            str: The name of the robot.
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        Set the name of the robot.

        Args:
            name (str): The new name for the robot.

        Raises:
            ValueError: If name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self.name = name

    def get_battery_level(self) -> int:
        """
        Get the battery level of the robot.

        Returns:
            int: The battery level of the robot.
        """
        return self.battery_level

    def set_battery_level(self, battery_level: int) -> None:
        """
        Set the battery level of the robot.

        Args:
            battery_level (int): The new battery level for the robot.

        Raises:
            ValueError: If battery_level is not an integer within [0, 100].
        """
        if not isinstance(battery_level, int) or not (0 <= battery_level <= 100):
            raise ValueError("battery_level must be an integer between 0 and 100")
        self.battery_level = battery_level

    def get_status(self) -> str:
        """
        Get the status of the robot.

        Returns:
            str: The status of the robot ('idle', 'working', 'charging').
        """
        return self.status

    def set_status(self, status: str) -> None:
        """
        Set the status of the robot.

        Args:
            status (str): The new status for the robot.

        Raises:
            ValueError: If status is not one of 'idle', 'working', 'charging'.
        """
        if status not in ['idle', 'working', 'charging']:
            raise ValueError("status must be one of: 'idle', 'working', 'charging'")
        self.status = status
