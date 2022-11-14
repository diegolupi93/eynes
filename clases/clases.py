import math


class Circle:
    """ Circle Class
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

