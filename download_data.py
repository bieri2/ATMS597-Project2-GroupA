import requests
import datetime
import numpy as np
import pandas as pd
import calendar

def make_request(endpoint, payload=None):
    """
    Make a request to a specific endpoint on the weather API
    passing headers and optional payload.
    
    Parameters:
        - endpoint: The endpoint of the API you want to 
                    make a GET request to.
        - payload: A dictionary of data to pass along 
                   with the request.
    
    Returns:
        Response object.
    """
    
    return requests.get(
        f'https://www.ncdc.noaa.gov/cdo-web/api/v2/{endpoint}',
        headers={
            'token': 'DrNovCebRHLqoCTHswqBiilKuQqqXTnE'
        },
        params=payload
    )

def add_a_month(date):
    """
    A Python function that takes in a datetime object and returns
    the next month.
    
    Parameters:
        - date : Input Datetime object.
    
    Returns:
        Output Datetime object, with next month added.
    """    
    
    month = date.month - 1 + 1
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def stripes_inputs(siteid, start, end, tunit):
    """
    A Python function that takes in a Station ID, start Datetime,
    end Datetime, time unit and downloads the necessary data from
    the Global Historical Climatology Network.
    
    Parameters:
        - siteid : Station ID.
        - start : Start Datetime.
        - end : End Datetime.
        - tunit : time unit, may be either 'y' for year, 'm' for 
         month, 'w' for week or 'd' for day.
    
    Returns:
        GHCN dataset as specified that can then be read as a dataframe.
    """ 
    
    results = []
    while start < end :
          response = make_request(
              'data', 
              {
                  'datasetid' : 'GHCND', # Global Historical Climatology Network - Daily (GHCND) dataset
                  'locationid' : siteid, # NYC - 'CITY:US360019'
                  'startdate' : start,
                  'datatypeid' : 'TMAX',
                  'enddate' : start,
                  'units' : 'metric'
              }
          )

          if response.ok:
              # we extend the list instead of appending to avoid getting a nested list
              results.extend(response.json()['results'][0])

          # update the current date to avoid an infinite loop at a given time interval
          if (tunit=='y'):
               start += datetime.timedelta(days=365)
          elif (tunit=='m'):
               start += add_a_month(start)
          elif (tunit=='w'):
               start += datetime.timedelta(weeks=tdelta)
          else:
               start += datetime.timedelta(days=1)
    return results

starttime = datetime.date(2018, 1, 1)
endtime = datetime.date(2018, 1, 10)
data = stripes_inputs(siteid = 'CITY:US360019', start=starttime, end=endtime, tunit='d')

## Create data-frame:
df = pd.DataFrame(data)
df.head()
