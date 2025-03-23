
f = open("python_file/a.txt",'r')


#1234ansd3234
print(f.tell())#返回当前文件指针的位置
f.seek(2)#文件指针往后偏移两个位置
print(f.tell())

print(f.read())

f.close()
