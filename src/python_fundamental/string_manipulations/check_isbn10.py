# number should be 9 digits and as a string
def check_isbn_10(number: str) -> str:

	isbn_10_digit: int = 0
	
	# use enumerate() to ger index and value in this index
	for index, value in enumerate(number):
		isbn_10_digit += ((index + 1) * int(value))
		
	isbn_10_digit %= 11
		
	if isbn_10_digit == 10:
		isbn_10_digit = 'X'
	
	print(number+str(isbn_10_digit))

	return number + str(isbn_10_digit)
