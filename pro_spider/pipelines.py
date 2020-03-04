# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ProSpiderPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='123',db='test',charset='utf8')
        self.cursor = self.conn.cursor()
        self.create_sql = "create table info_weibo(authors varchar(255) not null,praise int(11) not null,repost int(11) not null,comment_nums int(11) not null,text varchar(255) not null)"
        self.cursor.execute(self.create_sql)
        self.conn.commit()
        print('成功')

    def process_item(self, item, spider):
        authors = item.get('authors')
        praise = int(item.get('praise')[3:])
        print(praise,type(praise))
        repost = int(item.get('repost')[3:])
        print(praise, type(praise))
        comment_nums = int(item.get('comment_nums')[3:])
        print(praise, type(praise))
        text = item.get('text')

        sql_insert="insert into info_weibo(authors,praise,repost,comment_nums,text)values(%s,%s,%s,%s,%s)"
        self.cursor.execute(sql_insert, (authors,praise,repost,comment_nums,text))
        self.conn.commit()
        return item

    def close_spier(self,spider):
        self.cursor.close()
        self.conn.close()



class tiebaPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='123',db='test',charset='utf8')
        self.cursor = self.conn.cursor()
        self.create_sql = "create table info_tieba(authors varchar(255),reply_nums int(11) not null,text varchar(255) not null)"
        self.cursor.execute(self.create_sql)
        self.conn.commit()
        print('成功')

    def process_item(self, item, spider):
        authors = item.get('authors')
        text = item.get('text')
        reply_nums = item.get('reply_nums')

        sql_ins="insert into info_tieba(authors,reply_nums,text)values(%s,%s,%s)"
        self.cursor.execute(sql_ins, (authors,reply_nums,text))

        self.conn.commit()
        print('成功')
        return item

    def close_spier(self,spider):
        self.cursor.close()
        self.conn.close()

