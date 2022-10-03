<h1>News classification project</h1>

<h2>Scraping articles</h2>
Spider scripts for scraping news articles from:
* https://www.indiatoday.in/politics PoliticsSpider.py
* https://timesofindia.indiatimes.com/topic/finance EconomicsSpider.py
* https://timesofindia.indiatimes.com/topic/crime-news CrimeSpider.py

Each script creates a sub folder and stores the articles into csv files. 

<h2>Dataset</h2>
Script name: load_data.py

This script creates the dataframe and save it as a pickled file for later use.

<h2>Classification</h2>
Script name: classify.py

This script creates a pipeline and trains it using pickled dataset

<h1>Howto</h1>

1) Run each spider script for scraping from news sites

Attention! CSS can be changed on the source website so needs check if it is still up-to-date
2) Run load_data.py

It will make/clean a data folder and save datasets to pickles
3) Run classify.py to build a model
