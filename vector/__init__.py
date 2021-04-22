#!/usr/bin/env python3
import math,yaml,sys
from . import operators
from . import multibit
class BadDimensionCountError(ValueError):pass
class Vector:
    def __init__(self,*values):
        self.values=values
        self.dim=len(values)
    def norm(self):  
        return math.sqrt(sum([i**2 for i in self.values]))
    def __repr__(self):
        return 'Vector('+repr(self.values).replace('(','').replace(')','')+')'
    def __iter__(self):
        return iter(self.values)
    def __truediv__(self,n):
        return Vector(*apply(self.values,operators.div_with(n)))
    def __mul__(self,n):
        return Vector(*apply(self.values,operators.mul_with(n)))
    def __add__(self,n):
        return Vector(*apply_zip(self.values,n.values,operators.add))
    def __sub__(self,n):
        return Vector(*apply_zip(self.values,n.values,operators.sub))
    def __getitem__(self,i):
        return self.values[i]

def safesum(one,*vectors):
    result=one
    for i in vectors:
        result=result+i
    return result
def mdvector(dc=3):
    class MultiDimensionVector(Vector):
        def __init__(self,*values):
            if len(values)!=dc:
                raise BadDimensionCountError(
                f'this vector is {dc}D, arguments {len(values)}D')
            super().__init__(*values)
    return MultiDimensionVector
def apply(a,b):
    return [b(i) for i in a]

def apply_zip(a,b,c):
    ind=0
    result=[]
    for i in a:
        result.append(c(i,b[ind]))
        ind+=1
    return result
def normalize(v,dc=3):
    return v/v.norm()
def normalize_all(l,dc=3):
    m=[]
    for i in l:
            m.append(list(normalize(mdvector(dc=dc)(*i),dc=dc)))
    return m

def normalize_from_yaml(filename,dc=3):
   
    with open(filename) as stream:
        return normalize_all(yaml.safe_load(stream))
def geta(a,b):
    return a*(-1)**b
def multi(la):
    l=[Vector(*i) for i in la]
    result=[]
    ind=0
    for i in multibit.multibit(len(l)):
        k=safesum(*apply_zip(l,i,geta))
        
        result.append(k.norm())

    return max(result)/len(l)
    
