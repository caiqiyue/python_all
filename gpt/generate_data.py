with open('train.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

train_datas = []
temp_data = ''
for line in lines:

    if line!='\n':
        line = line.strip()
        temp_data+=(line+'\t')
    else:
        train_datas.append(temp_data)
        temp_data=''



with open('dataset.txt','w',encoding='utf-8') as f:
    for train_data in train_datas:
        f.write(train_data+'\n')

