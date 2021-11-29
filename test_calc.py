#Test case for 6 days

import unittest
import task1

class TestProb(unittest.TestCase):
    def test_prob(self):
        result = task1.myfun(int(input("enter days:")))

        self.assertEqual(result[0],27,msg="Invalid Output")
        self.assertEqual(result[1],56,msg="Invalid Output")


if __name__ == '__main__':
    unittest.main()
