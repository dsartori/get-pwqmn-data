import requests
import json
import petl


const limit = 10000
# Get station info from the API
data = getOntarioData('858d74bb-5aa5-4578-a5a3-49e28c5445c5', limit)

# Get water quality data from the API
data = getOntarioData('37a5af99-95d4-497c-8a82-fce64f582d6c', limit)

# Save the data to a file
with open('pwqmn_data.json', 'w') as outfile:
    json.dump(data, outfile)

def getOntarioData(resource_id, limit=str(limit)):
    # loop API calls until all data is retrieved
    var flag = True
    var offset = 0
    var dataSet = []
    while flag:
        url = 'https://data.ontario.ca/api/3/action/datastore_search'
        params = dict(resource_id=resource_id, limit=limit)
        resp = requests.get(url=url, params=params,offset=offset)
        data = json.loads(resp.text)
        if data['result']['records'] == []:
            flag = False
            else:
                dataSet.append(data['result']['records'])
                offset += limit
    return data
