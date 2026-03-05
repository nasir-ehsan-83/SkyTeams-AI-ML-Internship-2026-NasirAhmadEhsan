# compute GCD of two numbers
def gcd(num1: int, num2: int) -> int :
	while num2 != 0:
		num1, num2 = num2, num1 % num2
	return num1

# compute LCM of two numbers
def lcm(num1: int, num2: int) -> int:
	return (num1 * num2) // gcd(num1, num2)
