from scrapy.spiders import Spider
from scrapy import Selector
from scrapy.http import Request
from ..items import AppItem


class ProductHuntSpider(Spider):
	name = "producthunt"
	allowed_urls = ["producthunt.com"]
	start_urls = ["http://producthunt.com"]


	def parse(self, response):
		hxs = Selector(response)
		posts = hxs.xpath('//div[@class="container"]/ul/li')
		for post in posts:
			tags = [text.lower() for text in post.xpath('.//span[@class="post-item--platform"]/text()').extract()]
			if 'iphone' in tags or 'ipad' in tags or 'android' in tags:
				item = AppItem()
				item['source'] = 'Producthunt'
				item['title'] = post.xpath('.//a[@class="post-item--text--name"]/text()').extract()[0]
				print item["title"]
				ref_link = post.xpath('.//a[@class="post-item--text--name"]/@href').extract()[0]
				yield Request("https://producthunt.com/{}".format(ref_link), 
				callback=self.parse_page_2, meta={'item': item})
			

		
	def parse_page_2(self, response):
		hxs = Selector(response)
		url = hxs.xpath("//a[@class='post-get-it-button--primary']/@href").extract()[0]
		return Request(
			url=url,
			callback=self.parse_end_page,
			meta={'item': response.meta['item']})
		
	def parse_end_page(self, response):
		item = response.meta['item']
		item['website'] = response.url.rstrip('ref=producthunt').rstrip('?')
		yield item






		
