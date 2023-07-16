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
for station in petl.values(leadTable, 'Collection Site'):
    # filter the table for the current station
    stationTable = petl.select(leadTable, lambda rec: rec['Collection Site'] == station)
    # generate the chart
    bcd_chart.generate(petl.values(stationTable, 'Collection Date'), petl.values(stationTable, 'Result'), station, 'Lead Concentration (ug/L)', station + '.png')

# Write the data to a csv file
petl.tocsv(leadTable, 'pwqmn_data.csv')
