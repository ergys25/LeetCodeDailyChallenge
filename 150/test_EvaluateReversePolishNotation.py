import unittest
from EvaluateReversePolishNotation import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_eval_rpn(self):
        # Test case 1: Small expression
        tokens1 = ["2", "1", "+", "3", "*"]
        self.assertEqual(self.solution.eval_rpn(tokens1), 9)

        # Test case 2: Large expression
        tokens2 = ["4", "13", "5", "/", "+"]
        self.assertEqual(self.solution.eval_rpn(tokens2), 6)

        # Test case 3: Medium expression
        tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+",
                   "5", "+"]
        self.assertEqual(self.solution.eval_rpn(tokens3), 22)

        # Test case 4: Empty expression
        tokens4 = []
        self.assertEqual(self.solution.eval_rpn(tokens4), 0)

        # Test case 5: Expression with only one token
        tokens5 = ["5"]
        self.assertEqual(self.solution.eval_rpn(tokens5), 5)

        # Test case 6: Expression with negative numbers
        tokens6 = ["-2", "3", "+"]
        self.assertEqual(self.solution.eval_rpn(tokens6), 1)

        # Test case 7: Expression with division by zero
        tokens7 = ["4", "0", "/"]
        self.assertRaises(ZeroDivisionError, self.solution.eval_rpn, tokens7)

        # Test case 8: Expression with invalid token
        tokens8 = ["2", "1", "+", "3", "*", "a"]
        self.assertRaises(ValueError, self.solution.eval_rpn, tokens8)


if __name__ == '__main__':
    unittest.main()
