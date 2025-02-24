import numpy as np
import torch
import torch.nn as nn


class ProbSparseAttention(nn.Module):
    def __init__(self,top_k):
        super(ProbSparseAttention,self).__init__()
        self.top_k = top_k
        
    def forward(self,query,key,value):
        """
        query 128,10,300
        """
        scores = torch.matmul(query,key.transpose(1,2))#128,10,10 获取注意力分数 128个样本， 每个样本由10个词表示，10个词中每个词与其它所有词的关系10x10
        top_k_scores,top_k_indicies = torch.topk(scores,dim=-1,k=self.top_k)#128,10,3   128,10,3 每行分数的前三个最大值
        sparse_scores = torch.zeros_like(scores)#稀疏注意力

        # 将 scores 按照 index 中的索引值复制到 sparse_scores 中
        for i in range(self.top_k):  #是一列一列的将最大值，赋值给sparse_attention
            sparse_scores = sparse_scores.scatter_(dim=-1, index=top_k_indicies[:,:,i:i+1], src=top_k_scores[:,:,i:i+1])
        attention_weights = nn.functional.normalize(sparse_scores)
        output = torch.matmul(attention_weights,value)
        return output
        
        

data = torch.randn(128,10,300)        
attention = ProbSparseAttention(top_k=3)

output = attention(data,data,data)
print(output)
        

