import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def perimeter(self):
        pass
    @abc.abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, x,y):
        self.l = x
        self.b=y
    # def area(self):
    #     print ('area: ', self.l*self.b)
    def perimeter(self):
        print ('perimeter: ', 2 * (self.l + self.b))
    
r = Rectangle(10,20)
r.perimeter()
# r.area()