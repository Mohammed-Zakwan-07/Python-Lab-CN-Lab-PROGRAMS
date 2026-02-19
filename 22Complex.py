class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real + other, self.imag)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real - other, self.imag)
        return NotImplemented
    
    def __radd__(self, other):
        # Support number + Complex
        return self.__add__(other)
    
    def __rsub__(self, other):
        # Support number - Complex
        return Complex(other - self.real, -self.imag)
    
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"
    
    def conjugate(self):
        return Complex(self.real, -self.imag)

# Demo
c1 = Complex(4, 5)
c2 = Complex(2, -3)
c3 = Complex(7, 0)

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c1 + c2 = {c1 + c2}")
print(f"c1 - c2 = {c1 - c2}")
print(f"10 + c1 = {10 + c1}")
print(f"5 - c2  = {5 - c2}")
print(f"Conjugate of c1 = {c1.conjugate()}")
print(f"c3 (pure real) = {c3}")
