import torch


data = torch.arange(0,100,10)
print(data,data.dtype)#int64 属于 Long

print(torch.min(data),data.min())

print(torch.max(data),data.max())


#mean无法处理 Long类型的数据,所以先转换为32位浮点
print(torch.mean(data.type(torch.float32)))

print(torch.sum(data),data.sum())


print(data.argmin())
print(data.argmax())