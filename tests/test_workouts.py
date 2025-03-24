import unittest
from data_fetch.workouts import get_exercises # type: ignore

class TestWorkoutAPI(unittest.TestCase):

    def test_valid_exercise_filtering(self):
        result = get_exercises("chest", equipment="dumbbells", difficulty="moderate")
        self.assertGreater(len(result), 0)

    def test_invalid_filters(self):
        result = get_exercises("unknown", equipment="random_device")
        self.assertEqual(len(result), 0)

    def test_duration_filter(self):
        result = get_exercises("legs", duration="short")
        self.assertGreater(len(result), 0)

    def test_body_part_filter(self):
        result = get_exercises("abs", body_part="core")
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
