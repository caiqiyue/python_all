import pymysql


conn = pymysql.connect(
    host = 'localhost',# 自建的 mysql服务端 的 ip地址
    user = 'root',#账户名
    passwd= '123456',#密码
    database = 'db6',#数据库
    charset = 'utf8' #返回的字符集（与创建该数据库的字符集最好一致）
)

cursor = conn.cursor()#游标

# sql = 'select * from userinfo where user="{user}" and pwd="{pwd}"'.format(user='caiqiyue',pwd='1234')#自己拼接sql语句会有 sql注入风险

sql = 'select * from userinfo where user=%s and pwd = %s'

rows = cursor.execute(sql,('caiqiyue','123456'))#让 execute拼接 mysql语句，可以过滤掉非法字符 防止 sql注入风险

#关闭所有链接
cursor.close()
conn.close()

if rows:
    print("链接成功")
else:
    print("连接失败")