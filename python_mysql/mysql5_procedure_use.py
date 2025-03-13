


import pymysql
import pymysql.cursors


conn = pymysql.connect(
    host = 'localhost',# 自建的 mysql服务端 的 ip地址
    user = 'root',#账户名
    passwd= '123456',#密码
    database = 'db5',#数据库
    charset = 'utf8' #返回的字符集（与创建该数据库的字符集最好一致）
)


cursor = conn.cursor()

#没有参数的存储过程
# cursor.callproc("p1")#执行 存储过程，p1是别人才mysql里面创建了一个p1存储过程，并返回了这个接口
# print(cursor.fetchall())

cursor.callproc('p2',(0,2,0))
#内部 传递的参数 是 @_p2_0 = 0  @_p2_1 = 2  @_p2_2 = 0 第三个是我们自己设置的 传出参数
cursor.execute('select @_p2_2;')
print(cursor.fetchone())#(1,) 把存储过程 中返回值接收到


cursor.close()
conn.close()