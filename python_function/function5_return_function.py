

def getFunc(flag):
    def sum(a,b):
        return a + b
    
    def minus(a,b):
        return a - b
    
    if flag == "+":
        return sum
    else:
        return minus
    
res = getFunc('+')(1,4)
print(res)