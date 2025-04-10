

import torch

x = torch.arange(1,10)
x_reshaped = x.reshape(1,9)

print(x_reshaped,x_reshaped.shape)

#去除，所有为1的维度  1x9 --->  9,   A,1,B ---> A,B
print(x_reshaped.squeeze().shape)

#在第 dim 处 增加一个值为1 的维度
print(x_reshaped.squeeze().unsqueeze(dim=1).shape)


image_data = torch.rand(size=(28,28,3))

print(image_data.shape)

#按照指定要求，改变维度顺序
print(image_data.permute(2,1,0).shape)