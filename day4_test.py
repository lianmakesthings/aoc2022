import unittest
import day4

class TestDay4(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day4.part1('day4_test_input.txt'), 2)

    def test_part2(self):
        self.assertEqual(day4.part2('day4_test_input.txt'), 4)

if __name__ == '__main__':
    unittest.main()