import unittest
import task_one


class MyTestCase(unittest.TestCase):
    def test_sum_collector(self):
        self.assertEqual(21, task_one.sum_collector([1, 2, 3, 4, 5, 6]))  # add assertion here

    def test_list_returns_elements(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], task_one.list_creator())

    def test_list_duplicates_inserting(self):
        list2 = [1, 1, 2, 2, 3, 3, 4, 4]
        self.assertEqual(list2, task_one.duplicate_creator([1, 2, 3, 4]))

    def test_eliminate_duplicates(self):
        self.assertEqual([1, 2, 3, 4], task_one.eliminate_duplicates([1, 2, 3, 1, 3, 4, 4]))

    def test_third_elements_are_added(self):
        self.assertEqual([3, 6, 9], task_one.add_Third_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test_sun_middle_first_last(self):
        self.assertEqual(14, task_one.get_sum([5, 2, 6, 4, 4, 4]))

    def test_sun_middle_first_last_odd(self):
        self.assertEqual(13, task_one.get_sum([5, 2, 4, 4, 4]))

    def test_remove_elements(self):
        self.assertEqual(5, task_one.remove_elements(5, [1, 2, 3, 4, 4, 5]))

    def test_remove_elements_2(self):
        self.assertEqual([1, 2, 3, 4, 4, 5, 6], task_one.remove_elements(6, [1, 2, 3, 4, 4, 5]))

    def test_intersection(self):
        self.assertEqual([3, 2, 1], task_one.intersect_two_list([3, 2, 4, 1], [5, 3, 9, 2, 1]))

    def test_split_strings(self):
        self.assertEqual('xycdgj abzjkl', task_one.split_strings('abcdgj', 'xyzjkl'))

    def test_ssplit_string2(self):
        self.assertEqual('xycdgj abzjkl', task_one.split_strings('abcdgj', 'xyzjkl'))