from .cleaning_robot import CleaningRobot
from .cooking_robot import CookingRobot

class MaintenanceRobot(CleaningRobot, CookingRobot):
    """
    A robot capable of performing maintenance tasks such as cleaning and cooking.

    Attributes:
    - name (str): Name of the robot.
    - battery_level (int): Current battery level of the robot.
    - status (str): Current operational status of the robot.
    - cleaning_tool (str): Tool used for cleaning tasks.
    - cooking_skill (str): Skill level for cooking tasks.
    """

    def __init__(self, name: str, battery_level: int, status: str, cleaning_tool: str, cooking_skill: str) -> None:
        """
        Initialize the MaintenanceRobot with specific attributes.

        Args:
        - name (str): Name of the robot.
        - battery_level (int): Initial battery level.
        - status (str): Initial status.
        - cleaning_tool (str): Tool for cleaning tasks.
        - cooking_skill (str): Skill level for cooking tasks.
        """
        CleaningRobot.__init__(self, name, battery_level, status, cleaning_tool)
        CookingRobot.__init__(self, name, battery_level, status, cooking_skill)

    def multi_task(self) -> None:
        """
        Perform multi-tasking operation, attempting cleaning and cooking tasks based on battery levels.
        """
        print(f"{self.name} starting multi-task operation.")

        # Perform cleaning task
        if self.battery_level >= 20:
            CleaningRobot.work(self)
        else:
            print(f"{self.name} cannot start cleaning task due to low battery.")

        # Perform cooking task
        if self.battery_level >= 30:
            CookingRobot.work(self)
        else:
            print(f"{self.name} cannot start cooking task due to low battery.")
