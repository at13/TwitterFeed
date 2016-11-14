import twitter
import sqlite3
import time
import json
import psycopg2
import urlparse
import os
from sqlalchemy.exc import IntegrityError

class HashTags:

	def init_db(self, tag):
		urlparse.uses_netloc.append("postgres")
		x = os.environ['DATABASE_URL']
		url = urlparse.urlparse(x)
		self.conn =  psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
		c = self.conn.cursor()
		c.execute('DROP TABLE IF EXISTS %s' %tag)
		c.execute( '''CREATE TABLE %s ( id BIGINT PRIMARY KEY, tweet text)''' % tag)
		self.id = 0
		

	def init_twitter_api(self):
		api = twitter.Api(consumer_key="consumer_key", consumer_secret="consumer_secret")
		return api

	def fetch_save(self, api, tag):
		while(True):
			tag1 = "#"+tag
			print ('xxxxxxxxx')
			#print tag, tag1
			twit = api.GetSearch(term=tag1)
			c = self.conn.cursor()
			#print twit
			for x in twit:
				print (x.text.encode("utf-8"))
				#print (x.id)
				try:
					p=c.execute('INSERT INTO startupIndia VALUES (%s,%s)',(x.id, x.text))
				except:
					print ("trying to reenter")
				print p
				self.conn.commit()
				self.id = self.id +1
			
			
			time.sleep(30)


	def __init__(self, tag):
		self.init_db(tag);
		api = self.init_twitter_api();
		self.fetch_save(api,tag);
