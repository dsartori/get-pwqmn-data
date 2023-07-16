import requests
import json

# function to flatten list of lists
def flattenList(listOfLists):
    flatList = []
    for x in listOfLists:
        for y in x:
            flatList.append(y)
    return flatList

def getOntarioData(resource_id, limit=100):
    # loop API calls until all data is retrieved
    flag = True
    offsetValue = 0
    dataSet = []
    outputData = []
    while flag:
        url = 'https://data.ontario.ca/api/3/action/datastore_search'
        params = dict(resource_id=resource_id, limit=limit, offset=offsetValue)
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        if data['result']['records'] == []:
            flag = False
        else:
            dataSet.append(data['result']['records'])
            offsetValue += limit
    return flattenList(dataSet)