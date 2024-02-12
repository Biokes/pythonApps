import unittest
import fire_drill


class MyTestCase(unittest.TestCase):
    def test_index_in_even_positions_sum_up(self):
        self.assertEqual(20, fire_drill.index_in_even_positions_sum_up([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test_index_in_odd_positions_sum_up(self):
        self.assertEqual(25, fire_drill.index_in_odd_positions_sum_up([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test_index_in_third_positions_multiplication(self):
        self.assertEqual(28, fire_drill.index_in_third_positions_multiplication([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))

    def test_index_in_third_positions_sum_up(self):
        self.assertEqual(12, fire_drill.index_in_third_positions_sum_up([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test_get_largest_elements(self):
        self.assertEqual(9, fire_drill.get_largest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test_get_smallest_elements(self):
        self.assertEqual(0, fire_drill.get_smallest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test_get_length(self):
        self.assertEqual(10, fire_drill.get_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test_function_can_get_length_of_list(self):
        self.assertEqual(3, fire_drill.function_can_get_length_of_list([1, 2, 3]))

    def test_function_can_get_list_doubled_in_length_and_values(self):
        self.assertEqual([1, 2, 3, 2, 4, 6],fire_drill.get_doubled_list([1, 2, 3]) )