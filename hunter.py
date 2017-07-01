import requests
from bs4 import BeautifulSoup
from mails_getter import getMails
from csv_maker import makeCsv

if __name__ == "__main__":
	mails = getMails("https://www.shopify.com/blog/6037086-40-stunning-ecommerce-stores-built-using-shopify")
	makeCsv(mails, "40_Stunning_Ecommers_Storees")