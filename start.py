from promotehour.spiders import betabound_scraper, betalist_scraper, producthunt_spider, startuplist_scraper, startuplister_scraper
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import Queue

q = Queue.Queue()
process = CrawlerProcess(get_project_settings())

crawlers = ["producthunt", "betabound","betalist", "startuplist", "startuplister"]

for crawler in crawlers:
	q.put(process.crawl(crawler))


q.join()
while True:
	try:
		process = q.get(timeout=1)
	except Exception, e:
		break
	else:
		process.start()
