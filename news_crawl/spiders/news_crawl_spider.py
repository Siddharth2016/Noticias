from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_crawl.items import NewsCrawlItem


class NewsCrawlSpider(CrawlSpider):
    name = "newscrawl"
    allowed_domains = ["hindustantimes.com"]
    start_urls = [
        "http://www.hindustantimes.com/"
         
    ]

    rules = (
        Rule(LinkExtractor(allow="http://www.hindustantimes.com/india-news"), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        self.log("Scraping: " + response.url)

        articles = response.xpath('//tr[@class="athing"]')

        for article in articles:
            item = NewsCrawlItem()
            item["link_title"] = article.xpath('td[@class="title"]/a/text()').extract()[0]
            item["url"] = article.xpath('td[@class="title"]/a/@href').extract()[0]

            yield item
