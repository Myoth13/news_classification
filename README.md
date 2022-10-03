<h1>News classification project</h1>
This project is made for scraping news articles from the two websites and building classification model with three labels: 
'politics', 'economics' and 'crimes'
<h2>Scraping articles</h2>
Spider scripts for scraping news articles from:

<ul>
<li>https://www.indiatoday.in/politics PoliticsSpider.py</li>
<li>https://timesofindia.indiatimes.com/topic/finance EconomicsSpider.py</li>
<li>https://timesofindia.indiatimes.com/topic/crime-news CrimeSpider.py</li>
</ul>

Each script creates a sub folder and stores the articles into csv files. 

<h2>Dataset</h2>
<b>Script name:</b> load_data.py

This script creates the dataframe and save it as a pickled file for later use.

<h2>Classification</h2>
<b>Script name:</b> classify.py

This script creates a pipeline and trains it using pickled dataset

<h1>Howto</h1>

1) Run each spider script for scraping from news sites

Attention! CSS can be changed on the source website so needs check if it is still up-to-date

2) Run load_data.py

It will make/clean a data folder and save datasets to pickles

3) Run classify.py to build a model
