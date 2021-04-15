"""
Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
"""
from enum import Enum,auto
class Car:
    class Area(Enum):
        CA = auto(),
        LA = auto(),
        NY = auto(),
        NJ = auto()
    
    def __init__(self,elements:list) -> None:
        self.n = -1
        self.length = len(elements)
        self.elements = elements
    
    def get_items(self):
        for ele in self.elements:
            if len(ele) == 6 and ele[:2] in self.Area.__members__ and all([x.isdigit() for x in ele[2:]]):
                yield ele
            else:
                yield 'invaild'

a = Car(['CA1234','BM1233','NY1234s','NJ1112',''])

for item in a.get_items():
    print(item)