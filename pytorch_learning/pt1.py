


import torch

scalar = torch.tensor(7)
print(scalar)
print(scalar.item())
print(scalar.ndim)

print("===============================================")

vector = torch.tensor([1,1,1,])
print(vector)
# print(vector.item()) 向量没有 item()
print(vector.shape)
print(vector[0])
print(vector.ndim)

print("===================================================")

matrix = torch.tensor([[1,2,3],[2,3,4]])
print(matrix)
print(matrix.ndim)
print(matrix[1])
print(matrix.shape)

print("=====================================================")

tensor = torch.tensor([[[1,2,3],[2,3,4],[1,3,3]]])
print(tensor)
print(tensor[0][0])
print(tensor.ndim)
print(tensor.shape)