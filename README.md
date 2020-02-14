# ATMS597-Project2-GroupA
Repository for Group A's submission for Project 2.

Group members: Carolina Bieri, Arka Mitra, Jesse Loveridge

## (1) Downloading the data:

This is done with the <b>stripes_inputs</b> function. This function download daily minimum and maximum temperature data for the specified period.

The <b>stripes_inputs</b> function and associated helper function are adapted from Stefanie Moline: https://github.com/stefmolin/Hands-On-Data-Analysis-with-Pandas/

Example: Specify the GHCND Station ID ('stationid'), user-specific token ('token), and desired start and end years ('start' and 'end').
   
   e.g., 
   
   startyear = 1910
   
   endyear   = 2019
   
   token     = 'xxxxexampletokenxxxx'
   
   data = <b>stripes_inputs</b>(stationid = 'CITY:US360019', token = token, start = starttime, end = endtime)
   
## (2) Processing the data/filling missing values:

This is done with the <b>make_dataframe</b> function. This function does a few things:

- Create a DataFrame using the input data, which should be a list of dictionaries returned from <b>stripes_inputs</b>.

- Use the 'date' column of the dataframe (which comes from the list of dictionaries) to define a DateTime index for the DataFrame.

- Resample the data using pandas.DataFrame.resample() to fill missing values with NaNs. 

Example call: 

df = <b>make_dataframe</b>(data)

## (3) Plotting the Climate Stripes/Time-Series:

This is done with the <b>plot_stripes</b> function. This program plots Climate Stripes following the procedure created by Ed Hawkins at the University of Reading: https://showyourstripes.info/

This function can be used to plot data at yearly, monthly, or weekly frequency. The frequency can be specified using the flag 'tunit'. Additionally, the user can opt to plot a time series with axis labels over the Climate Stripes by using the 'plot_tseries' flag. 

The function first resamples the data to yearly, monthly, or weekly means. Next, a baseline average using data from 1970 to 2000 is calculated. Standardized anomalies are obtained by calculating temperature anomalies using this baseline average and dividing by the standard deviation for the available data corresponding to all years before 2000. 

Because of the nature of these calculations, these functions are best suited to data with a long-term temporal record (at least 1970 onwards). 

Example Climate Stripes plots for two stations (one in Utah and one in New York) are included with the functions to demonstrate functionality. 
