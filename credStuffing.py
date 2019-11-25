import requests, sys, os, re, fileinput
requests.packages.urllib3.disable_warnings() 

#Globals, 
#Configurable globals, should be configured to match your environment
adminUser = 'admin'
adminPass = 'bigip123'
host = 'https://29.4.6.19'
loginUri = '/tmui/logmein.html'
hostUrl = host + loginUri
credRegex = '(?P<username>.*):(?P<password>.*)'
#End configurable globals



#Require Python v3 or greater
if sys.version_info[:3] < (3,0,0):

	print('requires Python >= 3.0.0')
	sys.exit(1)

###Get the name of the policy passed as a command line arg
if len(sys.argv) > 1:

	credFile=sys.argv[1]

else:
    
    print('Error requires a filename')
    sys.exit()
##


for line in fileinput.input([credFile]):

	matchCreds = re.match(credRegex,line)

	if matchCreds:
		
		#print(matchCreds.group('username'))
		#print(matchCreds.group('password'))
		dataCreds = '{\'username\':\'' + matchCreds.group('username') + '\',\'passwd\':\'' + matchCreds.group('password') + '\'}'
		print(dataCreds)
		response = requests.post(hostUrl,data=dataCreds,verify=False)
		print(response.text)
