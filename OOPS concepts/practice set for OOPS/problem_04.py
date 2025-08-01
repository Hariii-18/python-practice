# write a class 'complex' to represent complex numbers , along with overloaded operatorrs + and * which adds and multiplies them
class Complex:
    def __init__(self, real, imag):
        self.real = real      # Real part
        self.imag = imag      # Imaginary part

    def __add__(self, other):
        # Overloads the + operator
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # Overloads the * operator
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __str__(self):
        # Nicely formats the output for printing
        sign = '+' if self.imag >= 0 else ''
        return f"{self.real} {sign}{self.imag}i"

# Example usage
c1 = Complex(2, 3)   # 2 + 3i
c2 = Complex(1, 4)   # 1 + 4i

print("First Complex Number: ", c1)
print("Second Complex Number:", c2)

# Addition
sum_result = c1 + c2
print("Addition Result:      ", sum_result)

# Multiplication
product_result = c1 * c2
print("Multiplication Result:", product_result)
        
