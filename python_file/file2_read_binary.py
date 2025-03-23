


image_file = open('python_file/xx.png','rb')

image_content = image_file.read()


image_file.close()


an_file = open("python_file/xx2.png",'wb')


an_file.write(image_content[0:len(image_content) // 2])

an_file.close()