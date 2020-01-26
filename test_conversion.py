from hw1 import *

def test_answer():
	assert conversion(1) == "I"
	assert conversion(4) == "IV"
	assert conversion(9) == "IX"