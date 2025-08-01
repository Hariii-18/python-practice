# write a class vector representing a vector of n dimensions overloading the + and * operator which calculates the sum and the dot(.) product of them
class Vector:
    def __init__(self, components):
        self.components = components  # A list of coordinates (e.g., [1, 2, 3])

    def __add__(self, other):
        # Element-wise addition of two vectors
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimension to add.")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        # Dot product of two vectors
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimension for dot product.")
        dot_product = sum(a * b for a, b in zip(self.components, other.components))
        return dot_product  # Returns a scalar, not a Vector

    def __str__(self):
        return f"Vector({self.components})"

# Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Vector 1:", v1)
print("Vector 2:", v2)

# Vector addition
sum_vector = v1 + v2
print("Sum:      ", sum_vector)

# Dot product
dot_result = v1 * v2
print("Dot Product:", dot_result)
