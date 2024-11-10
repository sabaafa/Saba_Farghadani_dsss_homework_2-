import unittest
from math_quiz import get_random_number, get_random_operator, create_math_problem  # Adjust the imports based on updated function names

class TestMathGame(unittest.TestCase):

    def test_get_random_number(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Random number {rand_num} out of range {min_val}-{max_val}")

    def test_get_random_operator(self):
        """Test if the function returns a valid operator."""
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random outputs
            operator = get_random_operator()
            self.assertIn(operator, valid_operators, f"Operator {operator} is not valid")

    def test_create_math_problem(self):
        """Test if create_math_problem constructs problems correctly and returns the right answer."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 3, '*', '4 * 3', 12),
            (0, 1, '+', '0 + 1', 1),
            (9, 9, '-', '9 - 9', 0)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Expected problem '{expected_problem}', got '{problem}'")
            self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer}, got {answer}")

if __name__ == "__main__":
    unittest.main()
