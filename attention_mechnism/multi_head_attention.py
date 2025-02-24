import torch
import torch.nn as nn
import numpy as np

class MultiHeadAttention(nn.Module):
    def __init__(self,d_model,n_heads,d_k,batch_size):
        """
        d_model:每个词转化成的维度
        n_heads：分几个头
        d_k:query,key,value的维度
        """
        super(MultiHeadAttention,self).__init__()
        self.batch_size = batch_size
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_k
        self.W_Q = nn.Linear(d_model,d_k * n_heads,bias=False)#
        self.W_K = nn.Linear(d_model,d_k * n_heads,bias=False)
        self.W_V = nn.Linear(d_model,d_k * n_heads,bias=False)
        self.fc = nn.Linear(n_heads * d_k,d_model,bias=False)
        
    
    def forward(self,input_q,input_k,input_v):
        """
        input_q、input_k、input_v : batch_size,seq_len,d_model
        """
        #开始分头  （bs,len,d_model) * (d_model,heads * d_key) --> (bs,len,heads * d_key) --> (bs,heads,len,d_key)
        #每一个批次中的每个样本，分成 heads 份 尺寸为 （seq_len，d_key)的 key
        query = self.W_Q(input_q).view(self.batch_size,-1,self.n_heads,self.d_k).transpose(1,2)#128,8,10,256 batch_size,heads,seq_len,query_len
        key = self.W_Q(input_k).view(self.batch_size,-1,self.n_heads,self.d_k).transpose(1,2)#128,8,10,256 batch_size,heads,seq_len,key_len
        value = self.W_Q(input_v).view(self.batch_size,-1,self.n_heads,self.d_k).transpose(1,2)#128,8,10,256 batch_size,heads,seq_len,key_len
        
        #缩放点积注意力
        scores = torch.matmul(query,key.transpose(-1,-2)) / np.sqrt(self.d_k)#128,8,10,10 batch_size,heads,seq_len,seq_len
        attention = torch.matmul(scores,value)#128,8,10,256 batch_size,heads,seq_len,value_len
        
        #通过，连接层 合并头
        attention = attention.transpose(1,2)
        attention = attention.reshape(self.batch_size,-1,self.n_heads * self.d_k)
        
        output = self.fc(attention)
        return output
    
attention = MultiHeadAttention(300,8,256,128)

data = torch.randn((128,10,300))
print(data.shape)
output = attention(data,data,data)
print(output)