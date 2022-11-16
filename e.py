import requests
import json
from concurrent.futures import ThreadPoolExecutor

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE+"Verify & Clean Bulk Email Lists"+bcolors.ENDC)
print("\n")
print(bcolors.FAIL+"Try it free ! www.8levellookup.online"+bcolors.ENDC+"\n")

apikey = input('API KEY :')
username = input('Username: ')
emailList = input("Email List Input :")


EmailList = open(emailList, "r")

for email in EmailList:

    email = email.strip()
    
    params = {'user':username,'apikey':apikey,'email':email}

    url = "http://8levellookup.online/app/email/"

    res = requests.get(url, params=params)
    response = json.loads(res.text)

    if response['api_status'] == 0 or response['api_hit'] > response['api_limit']:
        print ("api limite")
        exit()
    else:
        if response['email_extra_validate'] == 'successful' and response['email_format_validate'] == 1 and response['email_disposable'] == 0 and response['email_domain_validate'] == 1:
            print(bcolors.OKGREEN+response['email']+" Valid"+bcolors.ENDC)
            with open("valid.txt","a") as file:
                file.write(response['email']+"\n")
        elif response['email_format_validate'] == 1 and response['email_disposable'] == 0 and response['email_domain_validate'] == 1:
            print(bcolors.FAIL+response['email']+" Bounced"+bcolors.ENDC)
            with open("bounced.txt","a") as file:
                file.write(response['email']+"\n")
        else:
            print(bcolors.WARNING+response['email']+" Not valid"+bcolors.ENDC)
            with open("notvalid.txt","a") as file:
                file.write(response['email']+"\n")