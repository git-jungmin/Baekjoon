import math
from functools import reduce
def lcm(a,b):
    return a * b // math.gcd(a,b)
def lcm_multiple(l):
    return reduce(lcm,l)
def solution(arr):
    return lcm_multiple(arr)