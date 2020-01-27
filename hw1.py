#EC500 Building Software
#HW1 Alex Fatyga
#arabic number to roman numeral function

def conversion(arabic):

	if not isinstance(arabic,int):	#returns error string on errors
		return "ERROR - not an int"
	if arabic < 1 or arabic > 4000:
		return "ERROR - not within range"

	nums = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL", 
        50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
	roman = ""
	for val, numeral in sorted(nums.items(), reverse=True):
		while arabic >= val:
			arabic -= val #subtracts the arabic value by the highest value in nums and adds its associated roman numeral to the string
			roman += numeral
	return roman	#returns roman numeral in a string

#arabic = input("Enter your arabic number: ") #previously allowed users to input their value after running the file
#roman = conversion(int(arabic))
#print(roman)