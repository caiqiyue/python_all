
import pandas as pd
data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], 
        ['Albania', 'Europe', 28748, 2831741, 12960000000], 
        ['Algeria', 'Africa', 2381741, 37100000, 188681000000], 
        ['Andorra', 'Europe', 468, 78115, 3712000000], 
        ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
world = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})



# 注意一点， 好像 and or 在这里不太好用 但是 可以用 &  |  代表 和 或
#用 and or ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

rs = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
print(rs[['name','population','area']])