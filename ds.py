#-*-coding:utf-8-*-
import MySQLdb
class rrs:


    def select(self,sq):
        conn = MySQLdb.connect(host="localhost", user="root", passwd="924489503", db="chenxin", charset="utf8")
        cursor = conn.cursor()
        sql = sq
        n = cursor.execute(sql)
        conn.commit()#提交？
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def delete(self,sq):
        conn = MySQLdb.connect(host="localhost", user="root", passwd="924489503", db="chenxin", charset="utf8")
        cursor = conn.cursor()
        sql = sq
        n = cursor.execute(sql)
        conn.commit()  # 提交？
        cursor.close()
        conn.close()
        if n>0:
            return '删除成功'
        else:
            return '删除失败'


    def insert(self,sq):
        conn = MySQLdb.connect(host="localhost", user="root", passwd="924489503", db="chenxin", charset="utf8")
        cursor = conn.cursor()
        sql = sq
        n = cursor.execute(sql)
        conn.commit()  # 提交？
        cursor.close()
        conn.close()
        if n > 0:
            return '添加成功'
        else:
            return '添加失败'

    def update(self,sq):
         conn = MySQLdb.connect(host="localhost", user="root", passwd="924489503", db="chenxin", charset="utf8")
         cursor = conn.cursor()
         sql = sq
         n = cursor.execute(sql)
         conn.commit()  # 提交？
         cursor.close()
         conn.close()
         if n > 0:
             return '修改成功'
         else:
             return '修改失败'