"""Cálculo Matemático de Coseno."""
import math
def cos_sim(a, b):
    d = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x*x for x in a)); nb = math.sqrt(sum(y*y for y in b))
    return d/(na*nb) if na and nb else 0.0
print('Similitud:', cos_sim([1,0], [1,0]))
