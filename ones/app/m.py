from typing import List
from numpy.random import default_rng

rng = default_rng()

def init_seed(seed:int):
    global rng
    rng = default_rng(seed)

def choose_random_index( l: List[int], percentage:int) -> List[int]:
    global rng
    size = int(len(l)*percentage/100)
    if size==0: size = 1
    index = rng.integers(len(l), size=size )
    return list(index)

def choose_random_value(a:List[int])-> int :
    global rng
    value = rng.choice(a, size=1)[0]
    return value    

def choose_n_from_list(l:List[int], n:int) -> List[int]:
    global rng 
    values = list(rng.choice(l, size=n))
    return values
