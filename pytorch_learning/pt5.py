import torch


a = torch.tensor([1,2,3])
b = torch.tensor([2,3,4])

#element-wise multiply
print(a * b)


c = torch.tensor([[1,2,3],
                  [2,3,4],
                  [6,7,5]])

d = torch.tensor([[4,3,2],
                  [4,2,2]])

#matrix multiply three ways
print(torch.matmul(c,d.T))

print(c @ d.T)

print(torch.mm(c,d.T))

