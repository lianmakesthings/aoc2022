import unittest
import day2

class TestDay2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(15, day2.part1('day2_test_input.txt'))

    def test_part2(self):
        self.assertEqual(12, day2.part2('day2_test_input.txt'))


if __name__ == '__main__':
    unittest.main()