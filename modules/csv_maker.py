import csv

def makeCsv(mailsData, fileName):
	with open("files/" + fileName + ".csv", "w") as file:
		writer = csv.writer(file)
		writer.writerow(["shop url", "mails"])
		for data in mailsData:
			domain = data["domain"]
			mails = data["mails"]
			if(len(mails) == 0):
				writer.writerow([domain, "NOT FOUND"])
			else:
				writer.writerow([domain, mails[0]])
				for mail in mails[1:]:
					writer.writerow(["", mail])
		file.close()