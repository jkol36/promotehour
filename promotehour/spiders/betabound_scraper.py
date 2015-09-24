from scrapy.spiders import Spider
from scrapy import Selector
from scrapy.http import Request
from ..items import AppItem
from datetime import datetime



class BetaBoundScraper(Spider):
	name = "betabound"
	allowed_urls = ["betabound.com"]
	start_urls = ["http://betabound.com/android/", 'http://betabound.com/ios/']

	def parse(self, response):
		print "parsing"
		hxs = Selector(response)
		posts = hxs.xpath("//div[@id='gridlist']/article")
		
		for post in posts:
			item = AppItem()
			title = post.xpath("//h2[@class='opTitle']//a/text()").extract()[0]
			ref_link = post.xpath("//h2[@class='opTitle']//a/@href").extract()[0]
			item['title'] = title
			item['source'] = "betabound"
			item['mobile_checked'] = False
			item['date_added'] = datetime.today()
			yield Request(ref_link, meta={"item": item}, callback=self.parse_page_2)

	def parse_page_2(self, response):
		print "parsing page 2"
		item = response.meta['item']
		hxs = Selector(response)
		url = hxs.xpath("//a[@class='btn odBtn']/@href").extract()[0]
		item['website'] = url
		yield item