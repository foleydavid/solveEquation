import unittest
from Solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_combinationSum3(self):
        self.assertEqual(self.sol.solveEquation("x+5-3+x=6+x-2"), "x=2")
        self.assertEqual(self.sol.solveEquation("x=x"), "Infinite solutions")
        self.assertEqual(self.sol.solveEquation("2x=x"), "x=0")
        self.assertEqual(self.sol.solveEquation("2x+3x-6x=x+2"), "x=-1")
        self.assertEqual(self.sol.solveEquation("x=x+2"), "No solution")

if __name__ == "__main__":
    unittest.main()
