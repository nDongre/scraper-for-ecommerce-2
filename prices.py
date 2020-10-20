import scrapy
#from ..items import BluetomatoItem
import pandas as pd

#Custom settings for trying to get data to be scraped in proper order. Didn't work.
custom_settings = {
    'DEPTH_PRIORITY' : '1',
    'SCHEDULER_DISK_QUEUE' : 'scrapy.squeues.PickleFifoDiskQueue',
    'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeues.FifoMemoryQueue',
    'CONCURRENT_REQUESTS': '1' }

data = pd.read_csv('greendeck.csv')

urls = data['Product URL']
urls = urls.dropna()

url_list = list(urls)

class OneilSpider(scrapy.Spider):
    name = 'oneilspy'
    start_urls =  url_list

    def parse(self, response):

        product_price = response.css('body > div.page > div.container.product-detail.product-wrapper > div.row.product-detail__row-main > div.product-detail__basic-info.col-12.col-sm-6.col-md-4.col-xl-3.mb-sm-3.order-2 > div:nth-child(2) > div:nth-child(1) > div > div > span > span.sales > span::attr(content)').extract()

        yield{
            'product_price': product_price
        }

        
 

