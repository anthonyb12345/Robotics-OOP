from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name: str, battery_level: int, status: str, cleaning_tool: str) -> None:
        """
        Initialize a CleaningRobot object.

        Args:
            name (str): The name of the cleaning robot.
            battery_level (int): The initial battery level of the cleaning robot (0 to 100).
            status (str): The initial status of the cleaning robot ('idle', 'working', 'charging').
            cleaning_tool (str): The tool used by the cleaning robot ('vacuum' or 'mop').

        Raises:
            ValueError: If name is not a string, battery_level is not an integer within [0, 100],
                        status is not one of 'idle', 'working', 'charging', or cleaning_tool is not
                        one of 'vacuum' or 'mop'.
        """
        super().__init__(name, battery_level, status)
        if cleaning_tool not in ['vacuum', 'mop']:
            raise ValueError("cleaning tool must be one of: vacuum or mop")
        self.cleaning_tool = cleaning_tool

    def work(self) -> None:
        """
        Simulate the cleaning work of the cleaning robot.

        If the battery level is below 20%, the robot cannot work and its status becomes 'idle'.
        Otherwise, the robot's status is set to 'working', it performs cleaning for 20 battery units,
        and then sets its status back to 'idle'.

        Returns:
            None
        """
        if self.battery_level < 20:
            print("Cannot work because battery level is < 20")
            self.status = 'idle'
        else:
            self.status = 'working'
            print(f"{self.name} is cleaning")
            self.battery_level -= 20
            self.status = 'idle'


