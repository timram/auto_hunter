def getAnchors(soup):
	anchors = soup.find("div", class_="article__content").find_all("a")[1:]
	return filter(lambda a: not(a.get("href").find("leadpages") >= 0 or 
		a.get("href").find("11863377") >= 0), anchors)
