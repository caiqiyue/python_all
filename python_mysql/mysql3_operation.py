import pymysql


conn = pymysql.connect(
    host = 'localhost',# 自建的 mysql服务端 的 ip地址
    user = 'root',#账户名
    passwd= '123456',#密码
    database = 'db6',#数据库
    charset = 'utf8' #返回的字符集（与创建该数据库的字符集最好一致）
)




cursor = conn.cursor()


sql = 'insert into userinfo(user,pwd) values(%s,%s)'
# rows = cursor.execute(sql,('nihaoa','1234'))#返回受影响的行数，而非数据本身
# print(rows)

#插入多条记录
many_records = [('dasda','da'),('eqwewq','eqwe')]
rows = cursor.executemany(sql,many_records)
print(cursor.lastrowid)#可以返回在插入数据之前的 当前的记录id


conn.commit()#对于增删改，光执行sql语句，不会对数据库有任何实质影响，还需要commit下




cursor.close()

conn.close()