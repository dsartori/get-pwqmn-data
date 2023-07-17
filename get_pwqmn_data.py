import petl
import bcd_chart
import ontario_api

# Set the limit for the number of records to retrieve per request
limit = 10000

# Get station info from the API
stationTable = petl.fromdicts(ontario_api.getOntarioData('858d74bb-5aa5-4578-a5a3-49e28c5445c5', limit))

# Get water quality data from the API
observationTable = petl.fromdicts(ontario_api.getOntarioData('37a5af99-95d4-497c-8a82-fce64f582d6c', limit))

# Join the two tables
joinedTable = petl.join(observationTable,stationTable, lkey='Collection Site',rkey='STATION')

# filter joined table for lead analytes only
leadTable = petl.select(joinedTable, lambda rec: rec['Analyte'] == 'Lead')

# Generate a chart for each station
for station, name in petl.values(leadTable, 'Collection Site', 'NAME'):

    # filter the table for the current station
    stationTable = petl.select(leadTable, lambda rec: rec['Collection Site'] == station)

    # concatenate collection date and time into a single field
    stationTable = petl.addfield(stationTable, 'd', lambda rec: rec['Collection Date'] + ' ' + rec['Collection Time'])

    # sort the table by collection date 
    stationTable = petl.sort(stationTable, ['d'])

    # remove leading < symbol from result values
    stationTable = petl.convert(stationTable, 'Result', lambda v: int(v[1:]) if v[0] == '<' else v)
    
    # generate the chart
    bcd_chart.generate(petl.values(stationTable, ['Collection Date']), petl.values(stationTable, 'Result'), 'Lead Concentration (ug/L)', name,  station + '.png')

# Write the data to a csv file
petl.tocsv(leadTable, 'pwqmn_data.csv')
