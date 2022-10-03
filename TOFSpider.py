import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import datetime

class TOFSpider(scrapy.Spider):

    name = 'TOF_spider'

    def start_requests(self):
        urls = ['https://timesofindia.indiatimes.com/news']
        page_num = 100
        for page in range(1, page_num):
            urls.append('https://timesofindia.indiatimes.com/news/'+str(page))

        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('span.w_tle > a::attr(href)').extract()
        for link in links:
            if ('/business/' in link) or ('/india/' in link) or ('/city/' in link) :
                yield response.follow(url=link, callback=self.parse_story)
                #print(link)

    def parse_story(self, response):
        header = response.css('h1._1Y-96 > span::text').extract()
        description = response.css('div._3YYSt::text').extract()

        df = pd.DataFrame({'header': header, 'full': ' '.join(description)})
        file_name = 'data/text'+str(datetime.datetime.now())
        df.to_parquet(file_name)

process = CrawlerProcess()
process.crawl(TOFSpider)
process.start()
