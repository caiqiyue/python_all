import pymysql


conn = pymysql.connect(
    host = 'localhost',# 自建的 mysql服务端 的 ip地址
    user = 'root',#账户名
    passwd= '123456',#密码
    database = 'db6',#数据库
    charset = 'utf8' #返回的字符集（与创建该数据库的字符集最好一致）
)

cursor = conn.cursor()#游标

sql = 'select * from userinfo where user="{user}" and pwd="{pwd}"'.format(user='caiqiyue',pwd='1234')

rows = cursor.execute(sql)#执行mysql，返回的 是 rows

#关闭所有链接
cursor.close()
conn.close()

if rows:
    print("链接成功")
else:
    print("连接失败")