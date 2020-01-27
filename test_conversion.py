#EC500 Building Software
#HW1 Alex Fatyga
#test file of hw1.py

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
	assert hw1.conversion(104) == "CIV"
	assert hw1.conversion(493) == "CDXCIII"
	assert hw1.conversion(499) == "CDXCIX"
	assert hw1.conversion(500) == "D"
	assert hw1.conversion(999) == "CMXCIX"
	assert hw1.conversion(1021) == "MXXI"
	assert hw1.conversion(3000) == "MMM"
	assert hw1.conversion(3932) == "MMMCMXXXII"
	assert hw1.conversion(3999) == "MMMCMXCIX"

def test_abnormal(): #abnormal cases that should fail such as doubles, strings, ints below 1
	assert hw1.conversion(-1) == "ERROR - not within range"
	assert hw1.conversion(0) == "ERROR - not within range"
	assert hw1.conversion(-142) == "ERROR - not within range"
	assert hw1.conversion(-13295) == "ERROR - not within range"
	assert hw1.conversion(5121) == "ERROR - not within range"
	assert hw1.conversion("a") == "ERROR - not an int"
	assert hw1.conversion("testString") == "ERROR - not an int"
	assert hw1.conversion("12.1") == "ERROR - not an int"
	assert hw1.conversion(12.1) == "ERROR - not an int" 
	assert hw1.conversion(-2.5) == "ERROR - not an int"
