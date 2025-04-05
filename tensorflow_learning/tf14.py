import tensorflow as tf




"""
指数衰减学习率 = 初始学习率 * 学习率衰减率 ** （当前轮数 / 多少轮衰减一次）
"""

epochs = 40
lr_base = 0.2
lr_decay = 0.99
lr_step = 1

for epoch in range(epochs):
    lr = lr_base * lr_decay ** (epoch / lr_step)
    print(lr)