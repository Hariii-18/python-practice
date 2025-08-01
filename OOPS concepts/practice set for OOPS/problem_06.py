# write __str__() method to print the vector as follows : 7i + 8j + 10k
class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension.")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        if len(self.components) != 3:
            raise ValueError("This string format is only supported for 3D vectors.")
        return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"

# Example
v = Vector([7, 8, 10])
print(v)  # Output: 7i + 8j + 10k
