import scrapy


class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['https://marketdata.set.or.th/']
    start_urls = ['https://marketdata.set.or.th/']

    def parse(self, response):
        pass
