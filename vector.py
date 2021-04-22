#!/usr/bin/env python3
from vector import *


if __name__=='__main__':
    fname='vectors.yaml'
    if len(sys.argv)>2:
        if not sys.argv[2].startswith('--'):
            
            fname=sys.argv[2]
    out=multi(normalize_from_yaml(sys.argv[1]))
    print(out) 
