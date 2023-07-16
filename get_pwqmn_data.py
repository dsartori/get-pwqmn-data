import requests
import json
import petl

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

limit = 10000
# Get station info from the API
stationData = getOntarioData('858d74bb-5aa5-4578-a5a3-49e28c5445c5', limit)
# Get water quality data from the API
observationData = getOntarioData('37a5af99-95d4-497c-8a82-fce64f582d6c', limit)
stationTable = petl.fromdicts(stationData)
observationTable = petl.fromdicts(observationData)

# Join the two tables
joinedTable = petl.join(observationTable,stationTable, lkey='Collection Site',rkey='STATION')

# filter joined table for lead analytes only
leadTable = petl.select(joinedTable, lambda rec: rec['Analyte'] == 'Lead')

# Write the data to a csv file
petl.tocsv(leadTable, 'pwqmn_data.csv')
