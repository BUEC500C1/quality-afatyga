import hw1

def test_normal(): #correct, normal cases
	assert hw1.conversion(1) == "I"
	assert hw1.conversion(3) == "III"
	assert hw1.conversion(4) == "IV"
	assert hw1.conversion(9) == "IX"
	assert hw1.conversion(20) == "XX"
	assert hw1.conversion(24) == "XXIV"
	assert hw1.conversion(24) == "XXIV"
	assert hw1.conversion(99) == "XCIX"

def test_abnormal(): #abnormal cases that should fail such as doubles, strings, ints below 1
	assert hw1.conversion(-1) == "ERROR"
	assert hw1.conversion(0) == "ERROR"
	assert hw1.conversion(-142) == "ERROR"
	assert hw1.conversion(-13295) == "ERROR"
	assert hw1.conversion("a") == "ERROR"
	assert hw1.conversion("testString") == "ERROR"
	assert hw1.conversion("12.1") == "ERROR"
	assert hw1.conversion(12.1) == "ERROR" 
	assert hw1.conversion(-2.5) == "ERROR"
