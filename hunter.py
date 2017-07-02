import requests
from bs4 import BeautifulSoup
from modules.mails_getter import getMails
from modules.csv_maker import makeCsv
from importlib import import_module
import argparse

def url(value):
	if ((value.find("http://") == -1 and value.find("https://") == -1) or value.find(".") == -1 or 
	len(value) < 10):
		raise argparse.ArgumentTypeError("not valid url parameter: %s" %value)
	return value

def pythonModule(value):
	try:
		print(value)
		module = import_module(value)
		return module.getAnchors
	except ModuleNotFoundError:
		raise argparse.ArgumentTypeError("can't find python module: %s" %value)
	except AttributeError:
		raise argparse.ArgumentTypeError("can't find 'getAnchors' function in %s module" %value)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Extract mails from given url to given output file")
	parser.add_argument("-u", "--url", required=True, type=url)
	parser.add_argument("-o", "--output", required=True)
	parser.add_argument("-p", "--parser", required=True, type=pythonModule)
	parser.add_argument("-k", "--key", required=True)
	args = parser.parse_args()

	mails = getMails(args.url, args.parser, args.key)
	makeCsv(mails, args.output)