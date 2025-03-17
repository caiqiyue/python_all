







def outer(func):
    def inner(*args,**kwargs):
        print("-------------------------")
        
        res = func(*args,**kwargs)
        return res
    return inner



def test(num):
    # print(num)
    return num

rs = test(20)
print(rs)



    