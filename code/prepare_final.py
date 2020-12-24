from typing import Any, Collection
from typing import Any, Union, Optional, List

Number = Union[int, float, complex]

def catch_all(*args: Any, **kwargs: Any) -> None:
    return

def double_string(string: str, sep: str = '') -> str:
    return f'{string}{sep}{string}'

def my_abs(x: Number) -> Number:
    if x < 0:
        x = -x
    return x

def get_even(list_: List[int]) -> Optional[List[int]]:
    return

class ListBasedSet(Collection.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
overlap = s1 & s2            # The __and__() method is supported automatically