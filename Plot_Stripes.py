# Libraries needed to be imported
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import matplotlib as mpl

## Method to plot Climate (Warming) Stripes and/or Time Series (if asked) :
def plot_stripes(Tmax, Tmin, t, station_name, plot_tseries):
    """
    A Python function that takes in max/min data for a given station and 
    plots Climate Stripes and/or Time-Series, if user asks for one.
    
    Parameters:
        - Tmax : Array/List of Maximum Temperature Values.
        - Tmin : Array/List of Minimum Temperature Values.
        - t : Array/List of years in the record (might have multiple
          same values if there are monthly/weekly sub-data).
        - station_name : String name of the Station.
        - plot_tseries : Character variable with user choice for either
        plotting or not plotting Time-series line. Either 'y' or 'n'.
    
    Returns:
        Output Image as either a Climate Stripes with/without a time series.
    """  

    ## call figure and define plot titles
    fig = plt.figure(figsize=(8,6))
    plt.title(station_name, fontsize=14)
    ax = plt.gca()

    ## Calculate temporal intervals and temperature anomalies :
    num_t = len(np.unique(t))
    start = t[0]
    AvT = (Tmax+Tmin)/2
    Tav = []
    for i in np.arange(0,num_t):
        Tav.append(np.average(AvT[np.where(t==start+i)]))
    
    ## calculate anomalies
    MeanT = np.nanmean(Tav)
    Tanoms = Tav-MeanT

    ## Store the anomalies as a 2D matrix for the stripes: 
    heatmap = np.zeros((len(Tav),len(Tav)))
    for i in range(0,num_t):
        heatmap[:,i] = Tanoms[i]  

    ## calculate fraction of maximum T for the time-series :
    X = np.arange(num_t)
    points = Tav/np.nanmax(AvT)*len(Tav)

    ## Plot stripes and time-series if necessary :   
    plt.imshow(heatmap[:,:], origin = 'lower', cmap = 'seismic', vmin = np.nanmin(Tanoms), vmax = np.nanmax(Tanoms))
    if (plot_tseries == 'y'):
        plt.plot(X, points, marker = 'o', color='yellow') 
    plt.axis('off') # Suppress the axes
 
    # plt.savefig(station_name+'_ClimateStripes_'+str(start)+'_'+str(end)+'.png', bbox_inches='tight',dpi=400)
    plt.show()

## Read Example Data
station_name='Austin'
t = np.loadtxt('ClimateStripesData.txt', skiprows=2, usecols=[0])
Tmax = np.loadtxt('ClimateStripesData.txt', skiprows=2, usecols=[2])
Tmin = np.loadtxt('ClimateStripesData.txt', skiprows=2, usecols=[3])
plot_stripes(Tmax = Tmax, Tmin = Tmin, t = t, station_name = station_name, plot_tseries = 'y')

