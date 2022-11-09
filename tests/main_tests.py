import unittest

# import the class to be tested

import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
 
# now we can import the module in the parent
# directory.
from calculator import AlgebraCalculator

 
 
# equation = "1x + 5 = 10"
# main_obj = Calculator(equation)

class TestStringMethods(unittest.TestCase):
    main_obj = AlgebraCalculator()
    def test_calculate_equation_easy(self):
        equation = 'x + 5 = 10'
        self.assertEqual(self.main_obj.calculate_equation(equation), 5)
        
    def test_calculate_equation_meduim(self):
        equation = 'x - (5x + 2) = 50x'
        self.assertEqual(self.main_obj.calculate_equation(equation), "- 1/27")
        
if __name__ == '__main__':
    unittest.main()