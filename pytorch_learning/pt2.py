import torch


random_tensor = torch.rand(3,4)
print(random_tensor)
print(random_tensor.ndim)
print(random_tensor.shape)


image_tensor = torch.rand(size=(3,224,224))
print(image_tensor)
print(image_tensor.ndim)
print(image_tensor.shape)

zeros = torch.zeros(size=(4,4))
print(zeros)
print(zeros.ndim)
print(zeros.shape)

ones = torch.ones(size=(3,3))
print(ones)
print(ones.ndim)
print(ones.shape)

arange_tensor = torch.arange(start=1,end=100,step = 10)
print(arange_tensor)

zeros_like = torch.zeros_like(arange_tensor)
print(zeros_like)


ones_like = torch.ones_like(arange_tensor)
print(ones_like)