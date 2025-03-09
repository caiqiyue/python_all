import pymysql
import pymysql.cursors


conn = pymysql.connect(
    host = 'localhost',# 自建的 mysql服务端 的 ip地址
    user = 'root',#账户名
    passwd= '123456',#密码
    database = 'db6',#数据库
    charset = 'utf8' #返回的字符集（与创建该数据库的字符集最好一致）
)



cursor = conn.cursor(pymysql.cursors.DictCursor)#返回的结果以字典的形式表示

sql = 'select * from userinfo;'
rows = cursor.execute(sql)

print(rows)
print(cursor.fetchone())#{'id': 1, 'user': 'caiqiyue', 'pwd': '123456'}，取一条数据

print(cursor.fetchall())#取所有数据

print(cursor.fetchmany(size=2))#取指定量的数据

#注意，取数据的时候，游标cursor都会移动，就像读取文件数据一样，所以取完数据，游标也就停住，再次取就不会有数据了
#如果想  循环取数据  只有 让 游标 回退

cursor.scroll(3,mode='absolute')#退回到起点，并往下走三个，从第四个开始读取
print(cursor.fetchone())
cursor.scroll(1,mode='relative')#从当前的游标位置，往后跳一个，再开始取数据
print(cursor.fetchone())
cursor.close()
conn.close()