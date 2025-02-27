

import torch
import torch.nn as nn

class MultiLayerPerception(nn.Module):
    def __init__(self,input_dim,hidden_layer1_dim,hidden_layer2_dim,output_dim):
        super(MultiLayerPerception,self).__init__()
        self.hidden1 = nn.Linear(input_dim,hidden_layer1_dim)
        self.hidden2 = nn.Linear(hidden_layer1_dim,hidden_layer2_dim)
        self.fc = nn.Linear(hidden_layer2_dim,output_dim)
        self.sigmoid = nn.Sigmoid()
        self.relu = nn.ReLU()
        
    def forward(self,x):
        x = self.relu(self.hidden1(x))
        x = self.relu(self.hidden2(x))
        output = self.sigmoid(self.fc(x))
        return output
    
data = torch.randn(100,2)
mlp = MultiLayerPerception(2,16,8,2)
output = mlp(data)
print(output)
        
        