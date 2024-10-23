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