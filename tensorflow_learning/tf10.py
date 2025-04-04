from sklearn.datasets import load_iris
from pandas import DataFrame
import pandas as pd

x_data = load_iris().data#所有数据集中的所有输入特征，总共四个特征

y_data = load_iris().target#所有标签，总共三类

print(x_data)
print(y_data)

x_data = DataFrame(x_data,columns=['花萼长度','花萼宽度','花瓣长度','花瓣宽度'])

pd.set_option('display.unicode.east_asian_width',True)#列名对齐
print(x_data)

x_data['类别'] = y_data#新加一列
print(x_data)