import scrapy
from .. import items


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    # 要爬取的URL
    start_urls = ['https://finance.sina.com.cn/roll/index.d.html?cid=56592&page=1',
                  'https://finance.sina.com.cn/roll/index.d.html?cid=56592&page=2',
                  'https://finance.sina.com.cn/roll/index.d.html?cid=56592&page=3',
                  'https://finance.sina.com.cn/roll/index.d.html?cid=56592&page=4',
                  'https://finance.sina.com.cn/roll/index.d.html?cid=56592&page=5']

    # XPATH解析数据
    def parse(self, response, *args, **kwargs):
        title = response.xpath('//div[@class="listBlk"]/ul')
        for part in title:
            a = part.xpath('./li/a//text()').extract()
            item = items.FirstbloodItem()
            item['link'] = a
            yield item
