import hw1

def test_answer():
	assert hw1.conversion(1) == "I"
	assert hw1.conversion(4) == "IV"
	assert hw1.conversion(9) == "IX"
	assert hw1.conversion(-1) == ""
	assert hw1.conversion(0) == ""
