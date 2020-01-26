import hw1

def test_normal():
	assert hw1.conversion(1) == "I"
	assert hw1.conversion(3) == "III"
	assert hw1.conversion(4) == "IV"
	assert hw1.conversion(9) == "IX"
	assert hw1.conversion(20) == "XX"
	assert hw1.conversion(24) == "XXIV"
	assert hw1.conversion(24) == "XXIV"
	assert hw1.conversion(99) == "XCIX"

def test_abnormal():
	assert hw1.conversion(-1) == ""
	assert hw1.conversion(0) == ""
	assert hw1.conversion(-142) == ""
	assert hw1.conversion(-13295) == ""
	assert hw1.conversion("A") == ""
