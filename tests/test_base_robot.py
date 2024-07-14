import unittest
import sys
import os

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from robots.base_robot import Robot


class TestRobot(unittest.TestCase):
    def setUp(self):
        # Test implementation of the abstract Robot class
        class TestRobotImpl(Robot):
            def work(self):
                pass

        self.robot = TestRobotImpl("TestBot", 50, 'idle')

    def test_initialization(self):
        self.assertEqual(self.robot.get_name(), "TestBot")
        self.assertEqual(self.robot.get_battery_level(), 50)
        self.assertEqual(self.robot.get_status(), 'idle')

    def test_setters_and_getters(self):
        self.robot.set_name("NewName")
        self.assertEqual(self.robot.get_name(), "NewName")

        self.robot.set_battery_level(80)
        self.assertEqual(self.robot.get_battery_level(), 80)

        self.robot.set_status('working')
        self.assertEqual(self.robot.get_status(), 'working')

    def test_charge(self):
        self.robot.charge()
        self.assertEqual(self.robot.get_battery_level(), 100)
        self.assertEqual(self.robot.get_status(), 'idle')

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            self.robot.set_name(123)

    def test_invalid_battery_level(self):
        with self.assertRaises(ValueError):
            self.robot.set_battery_level(150)

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            self.robot.set_status('running')

if __name__ == "__main__":
    unittest.main()
