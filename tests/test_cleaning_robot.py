import unittest
import sys
import os

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CleaningRobot("CleanerBot", 50, 'idle', 'vacuum')

    def test_initialization(self):
        self.assertEqual(self.robot.get_name(), "CleanerBot")
        self.assertEqual(self.robot.get_battery_level(), 50)
        self.assertEqual(self.robot.get_status(), 'idle')
        self.assertEqual(self.robot.cleaning_tool, 'vacuum')

    def test_work(self):
        self.robot.work()
        self.assertEqual(self.robot.get_battery_level(), 30)
        self.assertEqual(self.robot.get_status(), 'idle')

        self.robot.set_battery_level(10)
        self.robot.work()
        self.assertEqual(self.robot.get_status(), 'idle')

    def test_invalid_cleaning_tool(self):
        with self.assertRaises(ValueError):
            CleaningRobot("CleanerBot", 50, 'idle', 'broom')

if __name__ == "__main__":
    unittest.main()
