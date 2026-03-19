import cmath # Handles both real and complex numbers

class QuadraticEquations:

    def __init__(self, a: float, b: float, c: float) -> None:
        self.__a: float = float(a)
        self.__b: float = float(b)
        self.__c: float = float(c)
        
        self.__root1: float
        self.__root2: float

        self.caluculate_roots()

    
    def get_a(self): return self.__a
    
    def get_b(self): return self.__b
    
    def get_c(self): return self.__c

    def get_root1(self):
        return self.__root1
    
    def get_root2(self):
        return self.__root2
    
    def get_discriminant(self) -> float:
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    
    def caluculate_roots(self) -> tuple:
        """Returns both roots as a tuple. Handles linear and complex cases."""
        # Case 1: Not a quadratic equation (a is 0)
        if self.__a == 0:
            if self.__b == 0:
                # No solution if both a and b are 0
                self.__root1 = None
                self.__root2 = None 
            
            self.__root1 = -self.__c / self.__b
            self.__root2 = None
        
        # Case 2: Standard quadratic formula
        d = self.get_discriminant()
        
        # We use cmath.sqrt so it works even if d is negative
        self.__root1 = (-self.__b + cmath.sqrt(d)) / (2 * self.__a)
        self.__root2 = (-self.__b - cmath.sqrt(d)) / (2 * self.__a)
