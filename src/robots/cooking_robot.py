from .base_robot import Robot

class CookingRobot(Robot):
    def __init__(self, name: str, battery_level: int, status: str, cooking_skill: str) -> None:
        """
        Initialize a CookingRobot object.

        Args:
            name (str): The name of the cooking robot.
            battery_level (int): The initial battery level of the cooking robot (0 to 100).
            status (str): The initial status of the cooking robot ('idle', 'working', 'charging').
            cooking_skill (str): The skill level of the cooking robot ('beginner', 'intermediate', 'expert').

        Raises:
            ValueError: If name is not a string, battery_level is not an integer within [0, 100],
                        status is not one of 'idle', 'working', 'charging', or cooking_skill is not
                        one of 'beginner', 'intermediate', 'expert'.
        """
        super().__init__(name, battery_level, status)
        if cooking_skill not in ['beginner', 'intermediate', 'expert']:
            raise ValueError("cooking skills must be one of: beginner, intermediate, expert")
        self.cooking_skill = cooking_skill

    def work(self) -> None:
        """
        Simulate the cooking work of the cooking robot.

        If the battery level is below 30%, the robot cannot work and its status becomes 'idle'.
        Otherwise, the robot's status is set to 'working', it performs cooking for 30 battery units,
        and then sets its status back to 'idle'.

        Returns:
            None
        """
        if self.battery_level < 30:
            print("Cannot work because battery level is < 30")
            self.status = 'idle'
        else:
            self.status = 'working'
            print(f"{self.name} is cooking")
            self.battery_level -= 30
            self.status = 'idle'

           