import torch


x = torch.arange(1,10)
print(x,x.shape)


x_reshaped = x.reshape(3,3)

print(x_reshaped,x_reshaped.shape)


x_viewd = x.view(1,9)
print(x_viewd,x_viewd.shape)

"""
reshape: reshape 方法创建一个新的张量，其元素与原始张量共享内存空间。这意味着改变形状后，原始张量和新的张量将共享相同的数据存储，所以在一个张量上的修改会影响到另一个张量。
view: view 方法并不会创建一个新的张量，而是返回一个与原始张量共享数据存储的新视图（view）。如果原始张量和新的视图张量上的元素被修改，它们会互相影响，因为它们共享相同的数据
"""

x_reshaped[0,0] = 5
print("x_reshaped,",x_reshaped,id(x_reshaped))
print("after change x_reshaped,x",x,id(x))
x_viewd[:,0] = 5
print(x_viewd,id(x_viewd))
print(x,id(x))


print(torch.stack([x,x,x,x],dim=1))#vstack or hstack
print(torch.stack([x,x,x,x],dim=0))