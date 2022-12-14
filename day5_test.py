import unittest
import day5

class TestDay4(unittest.TestCase):
    def test_build_ship(self):
        expected = [["Z", "N"], ["M", "C", "D"], ["P"]]
        self.assertEqual(day5.build_ship("day5_test_input_crates.txt"), expected)
    
    def test_parse_instructions(self):
        expected = [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
        self.assertEqual(day5.parse_instructions("day5_test_input_instructions.txt"), expected)

    def test_move_crates(self):
        test_cases = [{
            "crates": [["Z", "N"], ["M", "C", "D"], ["P"]],
            "instruction": (1, 2, 1),
            "expected": [["Z", "N", "D"], ["M", "C"], ["P"]]
        }]
        for test_case in test_cases:
            self.assertEqual(day5.move_crates(test_case["crates"], test_case["instruction"]), test_case["expected"])

    def test_part1(self):
        self.assertEqual(day5.part1("day5_test_input_crates.txt", "day5_test_input_instructions.txt"), "CMZ")

    def test_move_crates_together(self):
        test_cases = [
            {
                "crates": [["Z", "N"], ["M", "C", "D"], ["P"]],
                "instruction": (1, 2, 1),
                "expected": [["Z", "N", "D"], ["M", "C"], ["P"]]},
            {
                "crates": [["Z", "N", "D"], ["M", "C"], ["P"]],
                "instruction": (3, 1, 3),
                "expected": [[], ["M", "C"], ["P", "Z", "N", "D"]]
            }
        ]
        for test_case in test_cases:
            self.assertEqual(day5.move_crates_together(test_case["crates"], test_case["instruction"]), test_case["expected"])

    def test_part2(self):
        self.assertEqual(day5.part2("day5_test_input_crates.txt", "day5_test_input_instructions.txt"), "MCD")

if __name__ == '__main__':
    unittest.main()