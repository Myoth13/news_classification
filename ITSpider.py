import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import datetime

class ITSpider(scrapy.Spider):

    name = 'IT_spider'

    def start_requests(self):
        urls = ['https://www.indiatoday.in/india']
        page_num = 100
        for page in range(1, page_num):
            urls.append('https://www.indiatoday.in/india?page='+str(page))

        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('div.detail > h2 > a::attr(href)').extract()
        for link in links:
            if '/story/' in link:
                yield response.follow(url=link, callback=self.parse_story)

    def parse_story(self, response):
        header = response.css('article > div > h1::text').extract()
        short_text = response.css('div.story-kicker > h2::text').extract()
        descriptions = response.css('div.description > p::text').extract()
        full_text = ''

        for description in descriptions:
            full_text = full_text + description

        df = pd.DataFrame({'header': header, 'short': short_text, 'full': full_text})
        file_name = 'data/text'+str(datetime.datetime.now())+'IT.parquet'
        df.to_parquet(file_name)

process = CrawlerProcess()
process.crawl(ITSpider)
process.start()
