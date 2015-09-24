from scrapy.spiders import Spider
from scrapy import Selector
from scrapy.http import Request
from ..items import AppItem
from datetime import datetime



class StartupListScraper(Spider):
	name = "startuplist"
	allowed_urls = ["startupli.st"]
	start_urls = ["http://startupli.st"]

	def parse(self, response):
		print "parsing"
		hxs = Selector(response)
		posts = hxs.xpath("//div[@class='content']")
		
		for post in posts:
			item = AppItem()
			title = post.xpath("//div[@class='headline']//h3//a[@class='profile']/text()")[0].extract()
			item['title'] = title
			item['source'] = "startupli.st"
			ref_link = "http://startupli.st/{}".format(post.xpath("//div[@class='headline']//h3//a[@class='profile']/@href").extract()[0])
			item['mobile_checked'] = False
			item['date_added'] = datetime.today()
			yield Request(ref_link, meta={"item": item}, callback=self.parse_page_2)

	def parse_page_2(self, response):
		print "parsing page 2"
		item = response.meta['item']
		hxs = Selector(response)
		url = hxs.xpath("//a[@class='visit']/@href").extract()[0]
		print url
		item['website'] = url
		yield item