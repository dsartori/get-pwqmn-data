# get-pwqmn-data

A Python script written for Hackforge to demonstrate interaction with the Ontario Open Data Portal API. To learn more about Hackforge visit their [website](https://hackf.org).

The script file, get_pwqmn_data, uses petl to prep the data returned by the API for charting and generate the required images

The script relies on two small function modules:
* ontario_api.py contains a function to collect data chunks from the API via the requests module and flatten them into a single Python array of dictionaries
* bcd_chart.py contains a function to generate a simple line chart with matplotlib

There is a Dockerfile that can be used to generate a container for use with Visual Studio Code

