from google.protobuf.json_format import MessageToJson
import out.edadil_pb2 as e
import out_cities.edadel_cities_pb2 as e_city

from urllib.parse import urlparse, quote_plus
import requests
import sys
import json
import pprint
import os.path
import time

from sqlalchemy import create_engine, MetaData, Table
from datetime import datetime


update_dttm = datetime.now()
MAX_PAGE_NUMBER = 20 # max page to parse

def get_shops_by_city(city):
	"""Return vector of shops by city string"""
	#url = "https://api.edadeal.ru/web/localities/{}".format(city)
	url = "https://squark.edadeal.ru/web/localities/{}".format(city)
	data = requests.get(url, allow_redirects=True)
	data = data.content
	cities = e_city.Cities()
	#cities = cities
	cities.ParseFromString(data)
	jsonObj = MessageToJson(cities)
	data = json.loads(jsonObj)
	if "city" in data:
		res = [cur["name10"] for cur in data["city"]]
	else:
		print("LOG: Invalid json")
		return None
	return res
