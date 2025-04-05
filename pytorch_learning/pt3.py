
import torch

#float32为默认数据类型
float_32 = torch.tensor([3.0,6.0,9.0],dtype=None,
                                      device = None,
                                      requires_grad=False)

print(float_32)
print(float_32.dtype)

float_16 = float_32.type(torch.float16)
print(float_16.dtype)

int_32 = torch.tensor([3,6,9],dtype=torch.int32)

#不同的数据类型，进行运算时也可以；但还是需要注意神经网络中的不同tensor的数据类型
print(float_16 * int_32)

rdm_tensor = torch.rand(3,4)
print(rdm_tensor.size(),rdm_tensor.shape)
print(rdm_tensor.device)