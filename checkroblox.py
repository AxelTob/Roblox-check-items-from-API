import requests
import sys
import re
import json 
import os



if not os.path.exists('users.txt'):
	sys.exit('users.txt is not here ..')
if not os.path.exists('usersPrice.txt'):
	open('usersPrice.txt', 'w')
if not os.path.exists('rareitems.txt'):
	sys.exit('rareitems.txt is not here ..')

with open('users.txt', 'r') as users:
	for TARGETUSERNAME in users.readlines():
		TARGETUSERNAME = TARGETUSERNAME.strip()
		try:
			url = "https://api.roblox.com/users/get-by-username?username={0}".format(TARGETUSERNAME)
			getid = requests.get(url).text
			if '{"success":false' not in getid:
				userID = json.loads(getid)['Id']
		except:
			print("{0} : {1}".format(getid,TARGETUSERNAME))
            continue
		else:
			totalPrice = 0
			totalUrl = []
			for assetTypeId in ["2","3","8","9","10","11","12","13","17","18","19","21"]:
				url = 'https://www.roblox.com/users/inventory/list-json?assetTypeId={0}&itemsPerPage=100&pageNumber=1&sortOrder=Desc&userId={1}'.format(assetTypeId,userID)
				data = json.loads(requests.get(url).text)

				for x in data["Data"]["Items"]:
					try:
						if x["Product"]["NoPriceText"]:
							if["Product"]["NoPriceText"] == "Free":
								continue
							price = x["Product"]["NoPriceText"]
						else:
							if x['Product']['PriceInRobux'] == 'null':
								continue
							price = x["Product"]["PriceInRobux"]
							totalPrice += int(price)
					except TypeError:
						price = 'Offsale'
					with open('rareitems.txt','r') as rareitems:
						if x["Item"]["AbsoluteUrl"].split('/')[-1] in rareitems.read():
							totalUrl.append(x["Item"]["AbsoluteUrl"])
				print("User : {0} page {1} extract.".format(TARGETUSERNAME,assetTypeId))	
			print("\n\n")


			with open('usersPrice.txt', 'a') as data:
				data.write('{0} worth {1} robux item.\n'.format(TARGETUSERNAME,totalPrice))
				data.write('There are offsale items ! \n')
				for y in totalUrl:
					data.write(y+"\n")
				data.write("\n")
			print('User : {0} completely extract !'.format(TARGETUSERNAME))
