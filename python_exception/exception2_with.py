




f = open("xxx.jpg",'r')
f.readlines()
f.close()


try:
    f = open('xxx.jpg','r')
    f.readlines()
except Exception as e:
    print("",e)
    
finally:
    f.close()
    
    
"""
with语句就是  上下文语句 ，简化了 这个 try except
"""
with open("xx.jpg",'r') as f:
    f.readlines()