from twisted.internet import reactor
from promotehour.spiders import betabound_scraper, betalist_scraper, producthunt_spider, startuplist_scraper, startuplister_scraper
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import Queue

q = Queue.Queue()
runner = CrawlerRunner()

crawlers = [betabound_scraper.BetaBoundScraper, betalist_scraper.BetaListScraper, producthunt_spider.ProductHuntSpider, startuplister_scraper.StartupListerScraper, startuplist_scraper.StartupListScraper]

for crawler in crawlers:
	runner.crawl(crawler)

d = runner.join()
d.addBoth(lambda _:reactor.stop())
reactor.run()
#	q.put(process.crawl)


#q.join()
#while True:
#	process = q.get(timeout=1)
#	if process:
#		process.start()
#	else:
#		break
