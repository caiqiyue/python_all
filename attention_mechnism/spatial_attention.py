import torch
import torch.nn as nn
import torch.nn.functional as F

class SpatialAttention(nn.Module):
    def __init__(self, kernel_size=7):
        super(SpatialAttention, self).__init__()
        
        # 使用一个卷积层来生成空间注意力图
        self.conv = nn.Conv2d(2, 1, kernel_size=kernel_size, stride=1, padding=kernel_size//2, bias=False)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):#x:4,64,32,32
        # 计算输入特征图的平均值和最大值，沿着通道维度
        avg_out = torch.mean(x, dim=1, keepdim=True)#4,1,32,32 沿着通道 做平均池化
        max_out, _ = torch.max(x, dim=1, keepdim=True)#4,1,32,32， _返回的是最大值的位置
        
        # 将这两种信息拼接在一起作为卷积的输入
        x_cat = torch.cat([avg_out, max_out], dim=1)#4,2,32,32 平均池化 结果 +  最大池化结果
        
        # 通过卷积层得到空间注意力图
        attention_map = self.conv(x_cat)#4,1,32,32 (in=2,out = 1)的卷积
        
        # 使用Sigmoid函数归一化注意力图
        attention_map = self.sigmoid(attention_map)#4,1,32,32 注意力图 是 空间上的 代表 哪块 一个矩形区域哪块重要，哪块不重要
        
        # 将注意力图与原始输入进行逐像素相乘，得到加权后的输出
        out = x * attention_map
        
        return out
    
    
input_tensor = torch.randn(4, 64, 32, 32)

# 实例化空间注意力模块
spatial_attention = SpatialAttention(kernel_size=7)

# 得到带有空间注意力的输出
output_tensor = spatial_attention(input_tensor)

print(f"Input shape: {input_tensor.shape}")
print(f"Output shape: {output_tensor.shape}")