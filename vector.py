#!/usr/bin/env python3
import math,yaml,sys
class BadDimensionCountError(ValueError):pass
class Vector:
    def __init__(self,*values):
        self.values=values
        self.diam=len(values)
    def norm(self):  
        return math.sqrt(sum([i**2 for i in self.values]))
def mdvector(dc=3):
    class MultiDimensionVector(Vector):
        def __init__(self,*values):
            if len(values)!=dc:
                raise BadDimensionCountError(
                f'this vector is {dc}D, values {len(values)}D')
            super().__init__(*values)
    return MultiDimensionVector
def from_yaml_file(filename,dc=3):
    m=[]
    with open(filename) as stream:
        l=yaml.safe_load(stream)
        for i in l:
            m.append(mdvector(dc)(*l[i]).norm())
    return m
if __name__=='__main__':
    print(*from_yaml_file(sys.argv[1]),sep='\n',end='\n')
    
