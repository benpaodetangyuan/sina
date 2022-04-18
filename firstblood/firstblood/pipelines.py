# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql  # 导入pymql


class FirstbloodPipeline(object):
    connect = None
    cursor = None

    def process_item(self, item, spider):
        # 参数依次为IP地址，端口号，用户名，密码，数据仓库名,编码
        self.connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='117647', db='sina',
                                       charset='utf8')
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute('INSERT INTO sina(TEXT) VALUES("%s")' % (item['link']))
            self.connect.commit()
        except Exception as e:
            print(e)
            self.connect.rollback()
        self.cursor.close()
        self.connect.close()
        return item

