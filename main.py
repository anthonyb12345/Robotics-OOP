from src.robots.base_robot import Robot
from src.robots.cleaning_robot import CleaningRobot
from src.robots.cooking_robot import CookingRobot


robot1 = CleaningRobot("Robo",90,'idle','mop')
robot2 = CookingRobot("robo2",40,'charging','expert')
robot1.report_status()
robot2.charge()
robot1.work()
robot2.work()
robot2.report_status()
robot2.work()

