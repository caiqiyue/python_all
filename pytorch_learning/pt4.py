import torch


tensor = torch.tensor([1,2,3])

print(tensor + 10)
print(tensor * 10)
print(tensor - 10)


print(torch.mul(tensor,10))
print(torch.add(tensor,10))
print(torch.sub(tensor,10))