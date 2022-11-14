import math


class Circle:
    """ Circle Class

    Test of Circle
    repr
    >>> print(Circle(1))
    area: 3.141592653589793 perimeter:6.283185307179586

    Change radius
    >>> circle = Circle(1) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...
    >>> circle.radius = 10 # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...
    >>> print(circle)
    area: 314.1592653589793 perimeter:62.83185307179586

    Multiply
    >>> circle = Circle(1) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...
    >>> other_circle = circle * 10 # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    <BLANKLINE>
    ...
    >>> print(other_circle)
    area: 314.1592653589793 perimeter:62.83185307179586

    Bad Request number smaller than 0
    >>> circle = Circle(0) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    ValueError: The radius should be a number bigger than 0

    Bad Request not number
    >>> circle = Circle('asd') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    ValueError: The radius should be a number bigger than 0
    """
    def __init__(self, value=1):
        self._validate_value(value)
        self._radius = value
    
    def _validate_value(self, value):
        if not isinstance(value, (float, int)) or value <=0:
            raise ValueError("The radius should be a number bigger than 0")
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._validate_value(value)
        self._radius = value

    def area(self):
        return self._radius**2*math.pi
    
    def perimeter(self):
        return 2*self._radius*math.pi
    
    def __repr__(self) -> str:
        rep = f'area: {self.area()} perimeter:{self.perimeter()}'
        return rep
    
    def __mul__(self, value):
        self._validate_value(value)
        return Circle(self._radius * value)

if __name__ == "__main__":
    import doctest
    doctest.testmod()