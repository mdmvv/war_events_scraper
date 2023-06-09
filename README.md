# Scraping articles about the Russo-Ukrainian War from Reuters and Politico

The scraper collects text data about the Russo-Ukrainian war into reuters.csv and politico.csv files. With the current settings, the result is a set of 1000 texts (850 reuters and 150 politico) for about the last month.

Built using the `Scrapy`

Run:
scrapy crawl politico -O reuters.csv
scrapy crawl politico -O politico.csv
