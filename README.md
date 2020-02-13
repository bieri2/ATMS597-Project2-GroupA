# ATMS597-Project2-GroupA
Repository for Group A's submission for Project 2.

## (1) Downloading the data:

This is done with the <b> stripes_inputs </b> function.

The <b> stripes_inputs </b> function and associated helper function are adapted from Stefanie Moline: https://github.com/stefmolin/Hands-On-Data-Analysis-with-Pandas/

Example: Specify the GHCND Station ID ('stationid'), user-specific token ('token), and desired start and end years ('start' and 'end').
   
   e.g., 
   
   startyear = 1910
   
   endyear   = 2019
   
   token     = 'xxxxexampletokenxxxx'
   
   data = <b>stripes_inputs</b>(stationid = 'CITY:US360019', token = token, start=starttime, end=endtime)
   
## (2) Processing the data/filling missing values:

This is done with the <b> make_dataframe </b> function. This function does a few things:

- Create a DataFrame using the input data, which should be a list of dictionaries returned from <b> stripes_inputs </b>.

- Use the 'date' column of the dataframe (which comes from the list of dictionaries) to define a DateTime index for the DataFrame.

- Resample the data using pandas.DataFrame.resample() to fill missing values with NaNs. 

Example call: 

df = <b>make_dataframe</b>(data)
   

## (3) Plotting the Climate Stripes/Time-Series:

This is done with the <b>plot_stripes</b> program. 
   
   ## Self-sufficient enough. But the rest of the code has to be written in such a way that Plot_Stripes.py can have its necessary set of inputs, namely :
   
   (a) Tmax, Tmin (both of which are 1D Numpy Arrays/Lists), 
   
   (b) t (A 1D Numpy Array/List that has the time-stamp (year number or year-month combo) of each data. Here each time-stamp might be repeated multiple times, as there might be monthly or weekly data for annual records, whereas, there might be weekly or daily data for monthly records and so on).
   
   (c) Station_name - Self-explanatory. Used to title the plot only.
   
   (d) plot_tseries - A character user prompt that only plots the time-series on the stripes if the user inputs 'y'.
   
# Please edit the rest of the code and put these functions into one Python file.


