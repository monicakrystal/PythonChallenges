import loops  # The code to test
import unittest  # The test framework


class Loops_Tests(unittest.TestCase):
    def test_return_nums(self):
        self.assertEqual(loops.return_nums(1), [1])
    def test_return_nums_wrong(self):
        self.assertEqual(loops.return_nums(5), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
