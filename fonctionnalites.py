
def multiplication(a : int,b : int) -> int :

    """Multiply two numbers.

    This function takes two numerical inputs and returns their product. It is a simple utility for performing multiplication.

    Args:
        a (int or float): The first number to multiply.
        b (int or float): The second number to multiply.

    Returns:
        int or float: The product of the two input numbers.
    """

    return a * b

def division(a : float,b : float) -> float : 
    
    """
    Perform division of two numbers.

    This function takes two floating-point numbers and returns the result of dividing the first by the second. 
    If the second number is zero, it returns an error message indicating that division by zero is not possible.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division or an error message if division by zero is attempted.

    Raises:
        ZeroDivisionError: If the denominator is zero.

    Examples:
        >>> division(10, 2)
        5.0
        >>> division(10, 0)
        "Division par zéro impossible"
    """

    try :
        return a/b
    
    except ZeroDivisionError : 
        return "Division par zéro impossible"


def addition(a : float,b : float) -> float :
    
    """Calculate the sum of two numbers.

    This function takes two numerical inputs and returns their sum. It is a simple arithmetic operation that can handle both integers and floats.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

    Returns:
        int or float: The sum of the two input numbers.
    """

    return a + b

def soustraction(a : float,b : float) -> float :
    
    """Calculate the difference between two numbers.

    This function takes two numerical inputs and returns the result of subtracting the second number from the first. It is a straightforward arithmetic operation that can handle both integers and floats.

    Args:
        a (int or float): The number from which to subtract.
        b (int or float): The number to subtract.

    Returns:
        int or float: The difference between the two input numbers.
    """
    
    return a - b

