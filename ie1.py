import requests
def addhttp(ur):
	if "http://" not in ur:
		return "http://"+ur

url = raw_input("Enter an URL: ")
url = addhttp(url)

flag = True
getbool = True
try:
	rget = requests.get(url)
except:
	getbool = False
	print "GET Err"

try:
	roption= requests.options(url)
except:
	print "OPTIONS Err"
while flag:
	if(getbool == True):
		print "\n\n\n\n"
		print "0. Show all\n1. Show server application\n2. Show list of methods\n3. Show list of cookies\n4. Show cache information\n5. Show authentication information\n6. Show status\n7. Show type of connection\n8. End\n9. Change URL"
		num = input("Choose a number: ")
		print "\n"
	else:
		getbool = True
		num = 9
	
	if(num == 1 or num == 0):
		try:
			print "server app: ", rget.headers['server']
		except:
			print "Oops! server app Err"
	if(num == 2 or num == 0):
		try:
			print "server methods: ", roption.headers['public']
		except:
			print "Oops! server methods Err"
	if(num == 3 or num == 0):
		try:
			print "server cookies: ", rget.headers['set-cookie']	
		except:
			print "Oops! server cookies Err"
	if(num == 4 or num == 0):
		try:
			print "Expires: ", rget.headers['Expires']
		except:
			print "Oops! Expires Err"
		try:
			print "Last-Modified: ", rget.headers['Last-Modified']
		except:
			print "Oops! Last modified Err"
		try:
			print "Etag: ", rget.headers['etag']
		except:
			print "Oops! etag Err"
		try:
			print "Cache-control: ", rget.headers['cache-control']
		except:
			print "Oops! cache-control Err"
	if(num == 5 or num == 0):
		try:
			print "Authentication: ", rget.headers['WWW-Authenticate']
		except:
			print "Oops! Authentication Err"
	if(num == 6 or num == 0):
		try:
			print "Status: ", rget.status_code
			print "Status Err: ", rget.raise_for_status()
		except Exception as e:
			#print "Oops! Status Err"
			print e
	if(num == 7 or num == 0):
		try:
			print "Connection: ", roption.headers['connection']
		except:
			print "Oops! Connection Err"
	if(num == 8):
		flag = False
	if(num == 9):
		url = raw_input("Enter an URL: ")
		url = addhttp(url)
		try:
			rget = requests.get(url)
		except:
			getbool = False
			print "GET Err"
		try:
			roption= requests.options(url)
		except:
			print "OPTIONS Err"

