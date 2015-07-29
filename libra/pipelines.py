# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb as mysqldb

class LibraPipeline(object):

    hostname = 'localhost'
    user = 'root'
    password = '123456'
    database = 'aquarius_db'

    def process_item(self, item, spider):
        # conn = self.getConnection()
        # fields = [
        #     'developNumber', 'onlineDate', 'city', 'district',
        #     'turnover', 'popularity', 'income', 'divergence',
        #     'fluidity', 'transparency', 'datetime'
        # ]

        # data = []
        # for field in fields:
        #     data.append(item[field])
        # # data.append(item['platformId'])

        # # sqlStart = 'start transaction;'
        # insertDataSql = 'insert into tb_platform_total_rating(' + (',').join(fields) + ') value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        # insertRelSql = 'insert into tb_platform_platform_total_rating(platformId, ratingId) value(%s, last_insert_id());'

        # curs = conn.cursor()
        # curs.execute(insertDataSql, data)
        # curs.close()
        # curs = conn.cursor()
        # curs.execute(insertRelSql, [item['platformId']])
        # conn.commit()
        # curs.close()
        # conn.close()
        return item

    def getConnection(self):
        conn = mysqldb.connect(self.hostname, self.user, self.password, self.database)
        return conn
