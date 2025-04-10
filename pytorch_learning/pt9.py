import torch


x = torch.arange(1,10).reshape(1,3,3)
print(x,x.shape)

print(x[0])
print(x[0,0])


"""
tensor([1, 2, 3]) torch.Size([3])
tensor([[1, 2, 3]]) torch.Size([1, 3])
返回的，同样都是1 2 3  但是维度不同，所以要注意 : 的使用，可能返回值相同，但是维度是不一样的
"""
print(x[0][0],x[0][0].shape)
print(x[:,0,:],x[:,0,:].shape)

print(x[:,:,0],x[:,:,0].shape)
