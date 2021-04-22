def add(a,b):return a+b
def sub(a,b):return a-b
def mul(a,b):return a*b
def div(a,b):return a/b
def div_with(num):
    def divw(a):
        return a/num
    return divw
def mul_with(num):
    def divw(a):
        return a*num
    return divw
def sum_with(num):
    def divw(a):
        return a+num
    return divw
def sub_with(num):
    def divw(a):
        return a-num
    return divw


