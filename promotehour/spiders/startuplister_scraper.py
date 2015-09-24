from scrapy.spiders import Spider
from scrapy import Selector
from scrapy.http import Request
from ..items import AppItem
from datetime import datetime



class StartupListerScraper(Spider):
	name = "startuplister"
	allowed_urls = ["startuplister.com"]
	start_urls = ["http://startuplister.com/startups/"]
	ALLOWED_PLATFORMS = ['ios', 'android']


	def parse(self, response):
		hxs = Selector(response)
		posts = hxs.xpath("//div[@class='row startup']")
		for post in posts:
			item = AppItem()
			try:
				platform = post.xpath(".//p[@class='platform']/span/text()").extract()[0]
			except IndexError:
				continue
			if platform.lower() in self.ALLOWED_PLATFORMS:
				title = post.xpath(".//h2/text()").extract()[0]
				ref_link = post.xpath('@href').extract()[0]
				item['title'] = title
				item['source'] = "startuplister"
				item['mobile_checked'] = True
				item['date_added'] = datetime.today()
				yield Request(ref_link, meta={"item": item}, callback=self.parse_page_2)
	
	def parse_page_2(self, response):
		item = response.meta['item']
		hxs = Selector(response)
		website = hxs.xpath("//a[@class='btn voffset5 btn-default']/@href").extract()[0].split('?')[0]
		item = response.meta.get('item')
		item['website'] = website
		yield item



			
