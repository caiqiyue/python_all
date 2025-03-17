



#上下文管理器的嵌套，用逗号就行了
with open("xxx",'r') as from_file,open("xxx") as to_file:
    from_conten = from_file.readlines()
    to_file.write(from_conten)