import scrapy
from ..items import MoviesItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ImdbSpider(CrawlSpider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_1000&view=simple&sort=user_rating,desc']
    rules = (
                Rule(LinkExtractor(restrict_css='a.lister-page-next')),
                Rule(LinkExtractor(restrict_css='div.col-title'), callback='parse_item', follow=False))

    def parse_item(self, response):
        title = response.xpath('//h1/text()').get()
        self.logger.info("Found movie {}".format(title))
        cast_url = response.xpath("//li[@data-testid='title-pc-principal-credit']/a/@href").get()
        return response.follow(cast_url, self.parse_cast, cb_kwargs={'title': title})

    def parse_cast(self, response, title):
        directors = [ director.strip() for director in response.xpath("(//table[@class='simpleTable simpleCreditsTable'])[1]//td[@class='name']/a/text()").getall() ]
        cast = [ member.strip() for member in response.xpath("//table[@class='cast_list']//td[2]/a/text()").getall() ]
        return MoviesItem(title=title, directors=directors, cast=cast)

    #def parse(self, response):
        #titles = response.css('span.lister-item-header').xpath('.//a/text()').getall()
        #hrefs = response.css('span.lister-item-header').xpath('.//a/@href').getall()
        #print(titles)
        #for (title, link) in zip(titles, hrefs):
            #yield MoviesItem(title=title, link = link)