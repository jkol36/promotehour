from scrapy.spiders import Spider
from scrapy import Selector
from scrapy.http import Request
from ..items import AppItem



class BetaListScraper(Spider):
	name = "betalist"
	allowed_urls = ["betalist.com"]
	start_urls = ["http://betalist.com/startups"]

	def parse(self, response):
		print "parsing"
		hxs = Selector(response)
		posts = hxs.xpath("//div[@class='list content']//div[@class='startupGrid']//div[@class='startupGridItem']")
		
		i = 0
		for post in posts:
			item = AppItem()
			description = post.xpath("//a[@class='startupGridItem__pitch']/text()").extract()[i]
			if "mobile" or "app" or "ios" or "android" in description.lower():
				print "true"
				title = post.xpath("//a[@class='startupGridItem__name']/text()").extract()[i]
				ref_link = post.xpath("//div[@class='startupGridItem__image']//a/@href").extract()[i]
				item['source'] = "betalist"
				item["title"] = title
				item['website'] = "http://betalist.com" + ref_link + "/visit/"
				print description
				yield item
			i +=1
			
