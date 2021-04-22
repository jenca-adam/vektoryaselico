def dopln(m,le=2):
    if len(m)<le:
        return [0]*(le-len(m))+m
    return m
def dtob(l):
   return [int(i) for i in "{0:b}".format(l)]
def multibit_tonum(l,le=2):
    r=[]
    for i in range(l):
        r.append(dopln(dtob(i),le))
    return r
def multibit(l):
    return multibit_tonum(2**(l),l)
