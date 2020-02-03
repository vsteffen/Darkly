import scrapy
import requests, hashlib, logging, json
from scrapy import signals
from scrapy import Spider

logging.getLogger("chardet").setLevel(logging.WARNING)

readme_dict = {}


class BrickSetSpider(scrapy.Spider):
    name = 'spider42'
    start_urls = ['http://x.x.x.x/.hidden']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BrickSetSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        result_json = json.dumps(readme_dict)
        print '\n' + result_json + '\n'
        with open('result.log', 'w') as file_log:
            file_log.write(result_json)


    def parse(self, response):
        for next_page in response.css('a ::attr(href)'):
            # print 'Next link -> ' + next_page.get()
            if next_page is not None and next_page.get() != '../':
                if next_page.get() == 'README':
                    yield response.follow(next_page, callback=self.parse_item)
                yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response):
        page_url = response.request.url
        page = requests.get(page_url, stream = True)
        page_raw = page.text.encode('utf-8')
        page_hash = hashlib.md5(page_raw).hexdigest()
        if page_hash not in readme_dict:
            readme_dict[page_hash] = (page_url, page_raw)
