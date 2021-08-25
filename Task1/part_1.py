'''
Find : average precipitation in Hawaii, at 1:00 pm, on the 2nd of July 2000.

Datasets
URL : "https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets"
{
    "uid": "gov.noaa.ncdc:C00505",
    "mindate": "1970-05-12",
    "maxdate": "2014-01-01",
    "name": "Precipitation 15 Minute",
    "datacoverage": 0.25,
    "id": "PRECIP_15"
},
OR
{
    "uid": "gov.noaa.ncdc:C00313",
    "mindate": "1900-01-01",
    "maxdate": "2014-01-01",
    "name": "Precipitation Hourly",
    "datacoverage": 1,
    "id": "PRECIP_HLY"
}


Location
URL : "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ST&limit=52"
{
    "mindate": "1905-01-01",
    "maxdate": "2021-08-19",
    "name": "Hawaii",
    "datacoverage": 1,
    "id": "FIPS:15"
}


I tried getting hourly data of hawaii on july 2nd 2020 but data for 1pm was missing. (Using PRECIP_HLY)
URL : https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_HLY&units=metric&locationid=FIPS:15&startdate=2000-07-02&enddate=2000-07-03&limit=1000



So I got the data from PRECIP_15, which is the data collected every 15 minutes.
URL : https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_15&startdate=2000-07-02T12:00:00&enddate=2000-07-02T13:00:00&limit=1000&locationid=FIPS:15
'''

import requests
import json

def fetch_data(data_set_id, start_date, end_date, location_id):
    request_url = (base_url + "datasetid=" + data_set_id 
        + "&startdate=" + start_date + "&enddate=" + end_date 
        + "&locationid=" + location_id + "&limit=1000")
 
    page = requests.get(request_url, headers={'token': token})
    # TODO : Check response status Code. if its 2XX good. else throw exception.
    return page
    
def calculate_avg( data ):
    sum()

if __name__ == "__main__":
    
    token = "icdmBFbIAfneFugDjTdTmZKqxNLMepyX"
    base_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?"
    
    
    data_set_id = "PRECIP_15"
    start_date = "2000-07-02T12:00:00"
    end_date = "2000-07-02T13:00:00"
    location_id = "FIPS:15"
 
    # Fetch data from API
    page = fetch_data(data_set_id, start_date, end_date, location_id)
    
    # Get the content and
    content = page.content.decode("utf-8")
    formattedContent = json.loads(content)
    
    sum = 0
    counter = 0
    for i in formattedContent["results"]:
        # TODO : add method to check if the unit/metrics of mesurement is the same. ( Im not sure what V,,HT represents )
        sum += (i["value"])
        counter += 1
    
    print ("\n Average precipitation in Hawaii, at 1:00 pm, on the 2nd of July 2000 is : ", sum/counter, " V,,HT \n")