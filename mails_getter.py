import requests
from bs4 import BeautifulSoup
import json

apiKey = "fd640604d3e5066ef84c376494ba327fba466dcf"
baseUrl = "https://api.hunter.io/v2/domain-search?domain="
getInfo = lambda domain: json.loads(requests.get(baseUrl + domain + "&api_key=" + apiKey).text)

def getMails(url):

	def extractMails(domain):
		print("(%d) Extract mails for %s" %(domains.index(domain) + 1, domain))
		info = getInfo(domain)
		return list(map(lambda mail: mail["value"], info["data"]["emails"]))

	domains = _getDomains(url)
	print("Got %d domains to extract emails" %(len(domains)))
	return list(map(lambda domain: {"domain": domain, "mails": extractMails(domain)}, domains))

def _getDomains(url):
	html = requests.get(url).text
	soup = BeautifulSoup(html, "lxml")
	anchors = _getAnchors(soup)
	return list(set(map(lambda a: a.get("href").replace("shop.", ""), anchors)))

def _getAnchors(soup):
	anchors = soup.find("div", class_="article__content").find_all("a")[1:]
	return filter(lambda a: not(a.get("href").find("leadpages") >= 0 or 
		a.get("href").find("11863377") >= 0), anchors)
