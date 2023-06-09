from scrapy import Spider
from scrapy import Request


class ReutersSpider(Spider):
    name = 'reuters'

    def start_requests(self):
        for i in range(1, 86):
            page = f'https://www.reuters.com/news/archive/ukraine?page={i}'
            yield Request(page, callback=self.parse)

    def parse(self, response):
        for link in response.css('div.column1 div.story-content a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_event)

    def parse_event(self, response):
        title = response.css('h1.article-header__title__3Y2hh *::text').get().strip()
        text = ""
        for node in response.css('p.article-body__element__2p5pI *::text').getall():
            text += node.strip()
            text += '\n\n'
        yield {
            'Title': title,
            'Text': text,
            'Link': response.request.url
        }
