import os
import sys
from promotehour.spiders import betabound_scraper, betalist_scraper, producthunt_spider, startuplist_scraper, startuplister_scraper
from Queue import Queue
#	q.put(process.crawl)

q = Queue()
sites = ["producthunt", "betalist", "startuplist", "startuplister", 'betabound']
for site in sites:
	q.put(os.system("scrapy crawl {}".format(site)))

q.join()
while True:
	try:
		crawler = q.get(timeout=1)
	except Exception, e:
		break

	crawler.run()
