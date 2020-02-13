# ATMS597-Project2-GroupA
Repository for Group A's submission for Project 2.

## (1) Downloading the data:

This is done with the <b> stripes_inputs </b> functions. \n
The <b> stripes_inputs </b> and associated helper functions are adapted from Stefanie Moline: https://github.com/stefmolin/Hands-On-Data-Analysis-with-Pandas/

Example call:

<b> stripes_inputs </b>(stationid, token, start, end) 

Specify the GHCND Site ID ('stationid'), user-specific token ('token), and desired start and end years ('start' and 'end').
   
   e.g., 
   
   starttime = datetime.date(2018, 1, 1)
   
   endtime = datetime.date(2018, 1, 10)
   
   data = stripes_inputs(siteid = 'CITY:US360019', start=starttime, end=endtime, tunit='d')
   
   The download data can be read a Pandas data-frame,
   
   e.g.,
   
   import pandas as pd
   
   df = pd.DataFrame(data)
   
## (2) Processing the data/ Averaging it to the necessary time-interval:
   - I do this in the program for the example plot case in 'Plot_Stripes.py'. However, the downloaded data might not be averaged at the same time-interval as necessary for the stripes/time-series plot. An additional program must attend to that.
   
   ## Needs coding
   
## (3) Plotting the Climate Stripes/Time-Series:

   - I do this in the 'Plot_Stripes.py' program. 
   
   ## Self-sufficient enough. But the rest of the code has to be written in such a way that Plot_Stripes.py can have its necessary set of inputs, namely :
   
   (a) Tmax, Tmin (both of which are 1D Numpy Arrays/Lists), 
   
   (b) t (A 1D Numpy Array/List that has the time-stamp (year number or year-month combo) of each data. Here each time-stamp might be repeated multiple times, as there might be monthly or weekly data for annual records, whereas, there might be weekly or daily data for monthly records and so on).
   
   (c) Station_name - Self-explanatory. Used to title the plot only.
   
   (d) plot_tseries - A character user prompt that only plots the time-series on the stripes if the user inputs 'y'.
   
# Please edit the rest of the code and put these functions into one Python file.


