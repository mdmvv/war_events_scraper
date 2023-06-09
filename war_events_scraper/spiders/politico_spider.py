from scrapy import Spider
from scrapy import Request


class PoliticoSpider(Spider):
    name = 'politico'

    def start_requests(self):
        for i in range(1, 6):
            page = f'https://www.politico.eu/tag/war-in-ukraine/page/{i}'
            yield Request(page, callback=self.parse)

    def parse(self, response):
        for link in response.css('h2.card__title a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_event)

    def parse_event(self, response):
        title = response.css('h1.article-meta__title *::text, h2.headline *::text').get().strip()
        text = ""
        for node in response.css('div.article__content p *::text, p.story-text__paragraph *::text').getall():
            text += node.strip()
            text += '\n\n'
        yield {
            'Title': title,
            'Text': text,
            'Link': response.request.url
        }
