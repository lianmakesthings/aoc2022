import unittest
import day3

class TestDay2(unittest.TestCase):
    def test_find_dupes(self):
        test_data = {
            "p": ["vJrwpWtwJgWr","hcsFMMfFFhFp"],
            "L": ["jqHRNqRjqzjGDLGL","rsFMfFZSrLrFZsSL"],
            "P": ["PmmdzqPrV","vPwwTWBwg"],
            "v": ["wMqvLMZHhHMvwLH","jbvcjnnSBnvTQFn"],
            "t": ["ttgJtRGJ","QctTZtZT"],
            "s": ["CrZsJsPPZsGz","wwsLwLmpwMDw"],
            "r": ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"],
            "Z": ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        }

        for item_type in test_data:
            self.assertEqual(day3.find_duplicate_type(test_data[item_type]), item_type)

    def test_get_priority(self):
        test_data = {
            'p': 16,
            'L': 38,
            'P': 42,
            'v': 22,
            't': 20,
            's': 19,
        }
        
        for letter in test_data:
            self.assertEqual(day3.get_priority(letter), test_data[letter])

    def test_part1(self):
        self.assertEqual(day3.part1('day3_test_input.txt'), 157)

    def test_part2(self):
        self.assertEqual(day3.part2('day3_test_input.txt'), 70)

if __name__ == '__main__':
    unittest.main()