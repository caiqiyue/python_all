

import torch
import torch.nn as nn

class ChannelAttention(nn.Module):
    def __init__(self, in_channels,ratio):
        """
        in_channels图片的通道数
        ratio，通道数变化率
        """
        super(ChannelAttention,self).__init__()
        self.maxpool = nn.AdaptiveMaxPool2d(output_size=1)#全局最大池化，将 h,w 池化为1，1，就是在hxw个元素中挑选最大值
        self.avgpool = nn.AdaptiveAvgPool2d(output_size=1)#全局平均池化，将h,w 池化为1，1
        
        self.fc1 = nn.Linear(in_features=in_channels,out_features=in_channels // ratio,bias=False)#将通道数从 【b,c】 --> [b,c//4]
        
        self.fc2 = nn.Linear(in_features=in_channels//ratio,out_features=in_channels,bias=False)#将通道恢复到原大小
       
        self.relu = nn.ReLU()
        self.sigmoid =  nn.Sigmoid()
        
    def forward(self,x):
        b,c,h,w = x.shape
        #【b,c,h,w】 -- > [b,c,1,1]
        max_pool = self.maxpool(x)
        #[b,c,h,w] -- > [b,c,1,1]
        avg_pool = self.avgpool(x)
        #[b,c,1,1] -- >[b,c]
        max_pool = max_pool.view(b,c)
        #[b,c,1,1] -- > [b,c]
        avg_pool = max_pool.view(b,c)
        #[b,c] -- >[b,c//ratio]
        max_pool = self.fc1(max_pool)
        avg_pool = self.fc1(avg_pool)
        #[b, c //ratio]
        x_max_pool = self.relu(max_pool)
        x_avg_pool = self.relu(avg_pool)
        #[b , c//ratio] -- 》 [b,c]
        x_max_pool = self.fc2(x_max_pool)
        x_avg_pool = self.fc2(x_avg_pool)
        
        #[b,c] + [b,c]
        x_pool = x_max_pool + x_avg_pool
        #[b,c]
        x_pool = self.sigmoid(x_pool)
        #[b,c] -- > [b,c,1,1]
        x_pool = x_pool.view(b,c,1,1)
        
        #[b,c,1,1] x [b,c,h,w]
        outputs = x_pool * x
        
        return outputs
    
    

image = torch.randn((128,128,256,256))#模拟一批次数据 128张图片，每个图片128个通道，每个通道的图片大小为（256，256）
print(image.shape)
ca = ChannelAttention(128,4)

outputs = ca(image)

print(outputs.shape)


        
        
        
        