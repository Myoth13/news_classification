import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import datetime
from timeit import timeit
from pathlib import Path
import os, shutil
folder = 'data/crimes'

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


class CrimesSpider(scrapy.Spider):

    name = 'CrimesSpider'

    def start_requests(self):
        urls = ['https://timesofindia.indiatimes.com/topic/crime-news']
        page_num = 10
        for page in range(1, page_num):
            urls.append('https://timesofindia.indiatimes.com/topic/crime-news/'+str(page))

        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('div.Mc7GB > a::attr(href)').extract()
        for link in links:
         yield response.follow(url=link, callback=self.parse_story)

    @timeit
    def parse_story(self, response):
        header = response.css('h1._1Y-96 > span::text').extract()
        description = response.css('div._3YYSt::text').extract()
        full_text = ' '.join(description)
        short_text = ''
        df = pd.DataFrame({'header': header, 'short': short_text, 'full': full_text})
        file_name = folder + '/text'+str(datetime.datetime.now())+'.parquet'
        df.to_parquet(file_name)


process = CrawlerProcess()
process.crawl(CrimesSpider)
process.start()

