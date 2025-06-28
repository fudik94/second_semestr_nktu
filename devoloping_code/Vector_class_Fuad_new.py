class Vector:
    """Represents a 2D vector with x and y coordinates.

    Attributes:
        x (int or float): The x-coordinate of the vector.
        y (int or float): The y-coordinate of the vector.
    """

    def __init__(self, x: int, y: int):
        """Initializes a vector with given x and y values.

        Args:
            x (int or float): The x-coordinate.
            y (int or float): The y-coordinate.
        """
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        """Adds two vectors by summing their x and y components.

        Args:
            other (Vector): Another vector to add.

        Returns:
            Vector: A new vector with the summed coordinates.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: int) -> 'Vector':
        """Multiplies the vector by a scalar (incorrect operation, should be element-wise multiplication).

        Args:
            scalar (int or float): The scalar value to add (should be multiplied instead).

        Returns:
            Vector: A new vector with increased coordinates.
        """
        return Vector(self.x * scalar, self.y * scalar)


    def __str__(self) -> str:
        """Returns a string representation of the vector."""
        return f"({self.x}, {self.y})"

# Creating vectors
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Adding vectors
v3 = v1 + v2
print(v3)  # Output: (6, 8)

# Another example
v4 = Vector(-1, 7) + Vector(3, -2)
print(v4)  # Output: (2, 5)

# Scalar multiplication (incorrect implementation)
v5 = v1 * 2  # Should multiply, but currently adds the scalar
print(v5)  # Output: (4, 5), but expected (4, 6) if element-wise addition was intended
