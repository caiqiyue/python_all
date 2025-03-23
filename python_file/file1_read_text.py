

f = open(r'python_file\a.txt','r')
#open()返回的是一个文件对象，文件对象本质上就是一个文件句柄，就是一个通道，给你一个操作文件的窗口，mode就是通道的类型，规定通道的方向，
"""
只读，文件指针在开头，从头开始读
"""
content = f.read()
print(content)

f.close()



w = open('b.txt','w')
"""
只读：没有文件，则新建文件；指针在开头，从头开始往后写，会覆盖先前的内容
"""
w.write("abcd")
w.close()


a = open('b.txt','a')
"""
追加模式，文件指针在文件的结尾，从最后开始完后写内容，不会覆盖先前的内容
"""
a.write("adasd")
a.close()