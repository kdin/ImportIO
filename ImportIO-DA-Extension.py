# encoding: utf-8

import sys
import json
import requests
import easygui


requests.packages.urllib3.disable_warnings()
mode = ''

separator = ','
atEnd = '\n'

for i in range(len(sys.argv)):
	if str(sys.argv[i]).lower() == "-mode" and (i+1) < len(sys.argv):
		if str(sys.argv[i+1]).lower() == "preview":
			mode = 'PREVIEW';
		elif str(sys.argv[i+1]).lower() == "edit":
			mode = 'EDIT';
		elif str(sys.argv[i+1]).lower() == "refresh":
			mode = 'REFRESH';
	elif str(sys.argv[i]).lower() == "-size":
		size = sys.argv[i+1];



def getIndex(url):
	for index in range(0,len(url)):
		if(url[index+1] == '&' and url[index+2] == '_'):
			return index


def fetchData():

    url = easygui.enterbox(msg = 'Enter the URL + API KEY',title = 'URL+API KEY')


    pages = easygui.enterbox(msg = 'Enter the Max. pages to extract',title = 'MAX. PAGES TO EXTRACT')

    responses = []

    index = int(getIndex(url))

    for i in range(1, (int(pages)+1)):
        url = url[0:index] + str(i) + url[index+1:]
        response = requests.get(url,verify = False)
        response = json.loads(response.content)

        if i == 1 :
            result = response["results"]
            responses = responses + result
        else:
            result = response["results"]
            result.pop(0)
            responses = responses + result

    return responses


def formData(responses):
    firstObject = responses[0]
    keys = firstObject.keys()
    lastkey = keys[-1]
    data = ''
    for response in responses:
        for key in keys:

            if key != lastkey:
                data = data + response[key] + separator
            else:
                data = data + response[key] + atEnd
    return data

def supplyData(data):
    print "beginDSInfo"
    print "csv_first_row_has_column_names;true;true"
    print "csv_separator;,;true"
    print "endDSInfo"

    print "beginData"
    print data
    print "endData"

responses = fetchData()
data = formData(responses)

if mode == 'PREVIEW':
	supplyData(data)
elif mode == 'EDIT':
	supplyData(data)
elif mode == 'REFRESH':
	supplyData(data)