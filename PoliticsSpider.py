import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import datetime

from pathlib import Path
import os, shutil
folder = 'data/politics'

Path(folder).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


class PoliticsSpider(scrapy.Spider):

    name = 'PoliticsSpider'

    def start_requests(self):
        urls = ['https://www.indiatoday.in/politics']
        page_num = 10
        for page in range(1, page_num):
            urls.append('https://www.indiatoday.in/politics?page='+str(page))

        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('div.detail > h2 > a::attr(href)').extract()
        for link in links:
            yield response.follow(url=link, callback=self.parse_story)

    def parse_story(self, response):
        header = response.css('article > div > h1::text').extract()
        short_text = response.css('div.story-kicker > h2::text').extract()
        descriptions = response.css('div.description > p::text').extract()
        full_text = ''

        for description in descriptions:
            full_text = full_text + description

        df = pd.DataFrame({'header': header, 'short': short_text, 'full': full_text})
        file_name = folder + '/text'+str(datetime.datetime.now())+'.parquet'
        df.to_parquet(file_name)


process = CrawlerProcess()
process.crawl(PoliticsSpider)
process.start()
