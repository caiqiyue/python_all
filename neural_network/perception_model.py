



import torch
import torch.nn as nn


class PerceptionModel(nn.Module):
    def __init__(self,input_dim):
        super(PerceptionModel,self).__init__()
        self.W = nn.Linear(in_features=input_dim,out_features=1,bias=True)
        # self.sigmoid = nn.Sigmoid()
        self.sign = torch.sign()

    
    def forward(self,x):
        output = self.sign(self.W(x))
        return output
    

data = torch.randn(100,2)
labels = torch.randint(-1,1,(100,2))
perception = PerceptionModel(2)
output = perception(data)

print(output)