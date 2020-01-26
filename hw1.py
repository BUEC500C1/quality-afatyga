#arabic number to roman numeral

def conversion(arabic):

	nums = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL", 
        50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
	roman = ""
	for val, numeral in sorted(nums.items(), reverse=True):
		while arabic >= val:
			arabic -= val
			roman += numeral
	return roman

arabic = input("Enter your arabic number: ") #add error checking
roman = conversion(int(arabic))
print(roman)