import unittest
import gun


class MyTestCase(unittest.TestCase):
    def test_number_of_bullets(self):
        sniper = gun.Gun()
        self.assertEqual(0, sniper.count_bullet())

    def test_bullets_can_added_to_gun(self):
        sniper = gun.Gun()
        self.assertEqual(0, sniper.count_bullet())
        sniper.reload()
        self.assertEqual(10, sniper.count_bullet())

    def test_that_bullets_reduces_after_shooting(self):
        sniper = gun.Gun()
        self.assertEqual(0, sniper.count_bullet())
        sniper.reload()
        self.assertEqual(10, sniper.count_bullet())
        sniper.shoot()
        self.assertEqual(9, sniper.count_bullet())

    def test_that_bullets_can_be_reloaded_after_shooting(self):
        sniper = gun.Gun()
        self.assertEqual(0, sniper.count_bullet())
        sniper.reload()
        self.assertEqual(10, sniper.count_bullet())
        sniper.shoot()
        self.assertEqual(9, sniper.count_bullet())
        sniper.reload()
        self.assertEqual(19, sniper.count_bullet())

    def test_shooting_does_not_happen_if_there_is_no_bullet(self):
        sniper = gun.Gun()
        self.assertEqual(0, sniper.count_bullet())
        self.assertEqual("no bullet currently.", sniper.shoot())

    def test_that_can_shoot_while_there_is_bullet(self):
        sniper = gun.Gun()
        self.assertEqual(0, sniper.count_bullet())
        sniper.reload()
        self.assertEqual(10, sniper.count_bullet())
        for num in range(10):
            sniper.shoot()
        self.assertEqual("no bullet currently.", sniper.shoot())
