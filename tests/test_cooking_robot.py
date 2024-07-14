import unittest
import sys
import os

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from robots.cooking_robot import CookingRobot

class TestCookingRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CookingRobot("CookBot", 50, 'idle', 'intermediate')

    def test_initialization(self):
        self.assertEqual(self.robot.get_name(), "CookBot")
        self.assertEqual(self.robot.get_battery_level(), 50)
        self.assertEqual(self.robot.get_status(), 'idle')
        self.assertEqual(self.robot.cooking_skill, 'intermediate')

    def test_work(self):
        self.robot.work()
        self.assertEqual(self.robot.get_battery_level(), 20)
        self.assertEqual(self.robot.get_status(), 'idle')

        self.robot.set_battery_level(10)
        self.robot.work()
        self.assertEqual(self.robot.get_status(), 'idle')

    def test_invalid_cooking_skill(self):
        with self.assertRaises(ValueError):
            CookingRobot("CookBot", 50, 'idle', 'advanced')

if __name__ == "__main__":
    unittest.main()
