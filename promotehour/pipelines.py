# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
#import upload
from datetime import datetime

class PromotehourPipeline(object):

	def open_spider(self, spider):
		print 'Opened spider {}'.format(spider)
		with open('shit.csv', 'a+') as csvfile:
			writer = csv.writer(csvfile, lineterminator='\n')
			writer.writerow(['date_added', 'source', 'url', 'mobile_checked', 'name'])

	def write_to_csv(self, item):
		with open('shit.csv', 'a+') as csvfile:
			writer = csv.writer(open('shit.csv', 'a+'), lineterminator='\n')
			writer.writerow([item[key] for key in item.keys()])

		

	#add date to item
	def process_item(self, item, spider):
		self.write_to_csv(item)
		return item

	def close_spider(self, spider):
		pass
		#upload.upload_file()