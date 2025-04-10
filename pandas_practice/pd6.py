import pandas as pd


data1 = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]
employees = pd.DataFrame(data1, columns=['id', 'name']).astype({'id':'int64', 'name':'object'})
data2 = [[3, 1], [11, 2], [90, 3]]
employee_uni = pd.DataFrame(data2, columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})

print(employees)

print(employee_uni)

answer = pd.merge(employees,employee_uni,on='id',how='left')

print(answer[['unique_id','name']])