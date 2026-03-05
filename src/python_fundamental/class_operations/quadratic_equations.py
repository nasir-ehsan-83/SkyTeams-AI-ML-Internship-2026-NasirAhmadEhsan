import math

# quadratic equeation form ax2 + bx + c = 0
class QuadraticEquations:

    # __a, __b, and __c represent three coefficients.
    __a: float
    __b: float
    __c: float
    
    def __init__(self, a: float, b: float, c: float) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    # get_a() return coefficient of x2
    def get_a(self) -> float:
        return self.__a
    
    #get_b() return coefficient of x
    def get_b(self) -> float:
        return self.__b
    
    # get_c() return constant c
    def get_c(self) -> float:
        return self.__c
    
    # get_discriminant() return discriminant(b2 - 4*a*c) of equation
    def get_discriminant(self) -> float:
        return math.pow(self.__b, 2) - (4 * self.__a * self.__c)
    
    # get_root1() return the first root of equation
    def get_root1(self) -> float:
        
        # if the discriminant of equation is 0 or graeter there is first root
        if self.get_discriminant() >= 0:
            return (self.__b - math.sqrt(self.get_discriminant())) / (2 * self.__a)
        
        # if the discriminant of equation is less than 0 there is not any root
        else:
            return 0

    # get_root2() return second root of equation
    def get_root2(self) -> float:
        
        # if the discriminant of equation is graeter than 0 there is second root
        if self.get_discriminant() > 0:
            return -((- self.__b - math.sqrt(self.get_discriminant())) / (2 * self.__a))
        
        # if the discriminant of equation is 0 or less there is not any second root
        else:
            return 0
        
equa = QuadraticEquations(1, 5, 6)
print(equa.get_discriminant())
print(equa.get_root1())
print(equa.get_root2())