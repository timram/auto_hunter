import requests
from bs4 import BeautifulSoup
import json

def getMails(url, getAnchors, apiKey):
	def extractMails(domain):
		print("(%d) Extract mails for %s" %(domains.index(domain) + 1, domain))
		info = json.loads(requests.get(baseUrl + domain + "&api_key=" + apiKey).text)
		return list(map(lambda mail: mail["value"], info["data"]["emails"]))
	
	baseUrl = "https://api.hunter.io/v2/domain-search?domain="
	domains = _getDomains(url, getAnchors)
	print("Got %d domains to extract emails" %(len(domains)))
	return list(map(lambda domain: {"domain": domain, "mails": extractMails(domain)}, domains))

def _getDomains(url, getAnchors):
	html = requests.get(url).text
	soup = BeautifulSoup(html, "lxml")
	anchors = getAnchors(soup)
	return list(set(map(lambda a: a.get("href").replace("shop.", ""), anchors)))