from enum import Enum,auto
"""
Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, a Python iterator object must implement two special methods, __iter__() and __next__()

The question is that, given a list of car lisence plate, identify whether they are vaild through an iterator
"""
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

        
    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n < self.length:
            ele = self.elements[self.n]
            
            if ele[:2] in self.Area.__members__ and all([x.isdigit() for x in ele[2:]]) and len(ele)==6:
                return self.elements[self.n]
            else:
                return 'No Vaild!'
        else:

            raise StopIteration
print('Iteration 1')
for item in Car(['CA1234','BM1233','NY1234s','NJ1112','']):
    print(item)
print('Iteration 2')
a = Car(['CA1234','BM1233','NY1234s','NJ1112',''])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

