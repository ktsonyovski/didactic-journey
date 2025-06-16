"""A simple module providing basic mathematical operations."""

class MyMath:
    """
    A utility class for basic mathematical operations.

    This class provides static methods for addition, subtraction,
    multiplication, and division of two numbers.
    """

    @staticmethod
    def add(number1: int, number2: int) -> int:
        """
        Add two integers.

        Args:
            number1 (int): The first number to add.
            number2 (int): The second number to add.

        Returns:
            int: The sum of number1 and number2.

        Example:
            >>> MyMath.add(3, 5)
            8
        """
        return number1 + number2

    @staticmethod
    def substract(number1: int, number2: int) -> int:
        """
        Subtract the second integer from the first.

        Args:
            number1 (int): The number from which to subtract.
            number2 (int): The number to subtract.

        Returns:
            int: The result of number1 minus number2.

        Example:
            >>> MyMath.substract(10, 4)
            6
        """
        return number1 - number2

    @staticmethod
    def multiply(number1: int, number2: int) -> float:
        """
        Multiply two integers.

        Args:
            number1 (int): The first number to multiply.
            number2 (int): The second number to multiply.

        Returns:
            float: The product of number1 and number2.

        Example:
            >>> MyMath.multiply(3, 7)
            21.0
        """
        return number1 * number2

    @staticmethod
    def divide(number1: int, number2: int) -> float:
        """
        Divide the first integer by the second.

        Args:
            number1 (int): The numerator.
            number2 (int): The denominator.

        Returns:
            float: The result of number1 divided by number2.

        Raises:
            ZeroDivisionError: If number2 is zero.

        Example:
            >>> MyMath.divide(10, 2)
            5.0
        """
        return number1 / number2
