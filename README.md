# ATMS597-Project2-GroupA
Repository for Group A's submission for Project 2.

## (1) Downloading the data:

This is done with the <b>stripes_inputs</b> function.

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

This is done with the <b>plot_stripes</b> program. This program plots Climate Stripes following the procedure created by Ed Hawkins at the University of Reading: https://showyourstripes.info/


   
   (c) Station_name - Self-explanatory. Used to title the plot only.
   
   (d) plot_tseries - A character user prompt that only plots the time-series on the stripes if the user inputs 'y'.
   

