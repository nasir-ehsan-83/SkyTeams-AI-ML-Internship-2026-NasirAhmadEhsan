from typing import Optional

# compute GCD of two numbers
def gcd(num1: int, num2: int) -> Optional[int] :
	if num1 != 0 and num2 != 0:
		while num2 != 0:
			num1, num2 = num2, num1 % num2
		return num1
	else:
		return None
	
# compute LCM of two numbers
def lcm(num1: int, num2: int) -> Optional[int]:
	if num1 != 0 and num2 != 0:
		return (num1 * num2) // gcd(num1, num2)
	else:
		return None