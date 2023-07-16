import petl
import ontario_api

limit = 10000
# Get station info from the API
stationTable = petl.fromdicts(ontario_api.getOntarioData('858d74bb-5aa5-4578-a5a3-49e28c5445c5', limit))
# Get water quality data from the API
observationTable = petl.fromdicts(ontario_api.getOntarioData('37a5af99-95d4-497c-8a82-fce64f582d6c', limit))

# Join the two tables
joinedTable = petl.join(observationTable,stationTable, lkey='Collection Site',rkey='STATION')

# filter joined table for lead analytes only
leadTable = petl.select(joinedTable, lambda rec: rec['Analyte'] == 'Lead')

# Write the data to a csv file
petl.tocsv(leadTable, 'pwqmn_data.csv')
