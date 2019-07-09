import  scrapy
from ..items import Scraped_Item

class Quotespider(scrapy.Spider):

        name = 'Farm'
        start_urls = [
            'https://www.dhaanika.com/shop'
        ]

        def parse(self, response):
            item = Scraped_Item()

            name = response.css('._2BULo::text').extract()
            link = response.css('._2AHc6::attr(href)').extract()
            price = response.css('._23ArP::text').extract()

            item['name'] = name
            item['link'] = link
            item['price'] = price

            yield item

        # next_page = 'http://quotes.toscrape.com/page/'+str(Quotespider.page_number)+'/'
        # #response.css('li.next a::attr(href)').get()
        # #if next_page is not None:
        # if  Quotespider.page_number<=10:
        #     Quotespider.page_number+=1
        #     yield response.follow(next_page, callback = self.parse)
