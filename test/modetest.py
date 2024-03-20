from apps.task_and_assignment.mode import Mode


class TestMode:
    def test_mode(self):
        assert Mode.mode_value([1, 2, 3, 3, 4, 3]) == [3, 3]
        assert Mode.mode_value([2, 3, 3, 5, 6, 7]) == [2, 3]
