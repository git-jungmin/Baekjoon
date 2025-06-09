import math
def solution(numer1, denom1, numer2, denom2):
    d = denom1 * denom2 // math.gcd(denom1,denom2)
    n = numer1 * (d // denom1) + numer2 * (d // denom2)
    return [(n // (math.gcd(d,n))),(d // (math.gcd(d,n)))]