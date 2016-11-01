import numpy
import matplotlib
matplotlib.use("qt4agg", force=True)
from matplotlib import pyplot
from time import sleep
import sys
#from time import time

DATAFILE = "/home/brandon/temperature-desk.csv"

# timestamps
timestamps = []                    # empty array to hold x-data
COLUMN_TIMESTAMP = 0               # index of the timestamp column
SECONDS_PER_TIMESTAMP_VAL = 0.001  # 0.001 for timesteps in milliseconds
VIEW_WINDOW = 600                 # seconds of data to view at once
LOOP_DELAY = 0.01                  # seconds between main loop iterations
timepoint_delay = 0                # timestamp values between timepoints
file_position = 0                  # current position in the data file
window_rightbound = VIEW_WINDOW    # set the window's initial right bound

# data
TOTAL_COLUMNS = 3                      # total number of columns expected per datapoint
COLUMN_YDATA = [1]                     # index of the y-data columns
YMIN = 15.0                             # y-min for plotting
YMAX = 35.0                            # y-max for plotting
NUM_YCOLS = len(COLUMN_YDATA)          # number of y-data columns
ydata = [[] for n in range(NUM_YCOLS)] # empty array to hold y-data

# create an animated plot
pyplot.ion() 
fig1 = pyplot.figure()
ax1 = fig1.add_subplot('111')
fig1.suptitle('realtime sensor data', fontsize='18', fontweight='bold')
pyplot.xlabel('time, seconds', fontsize='14', fontstyle='italic')
pyplot.ylabel('temperature, degC', fontsize='14', fontstyle='italic')
pyplot.axes().grid(True)

plotlines = [pyplot.plot(ydata[n],marker='o',markersize=4,linestyle='none',markeredgewidth=0.0)[0]
                for n in range(NUM_YCOLS)]

pyplot.ylim([YMIN,YMAX])
pyplot.xlim([0,VIEW_WINDOW])
pyplot.show(block=False)

run = True

def get_time(timepoint):
    try:
        timeval = float(timepoint[COLUMN_TIMESTAMP])*SECONDS_PER_TIMESTAMP_VAL
        return timeval
    except: 
        print("bad timepoint: " + str(timepoint[COLUMN_TIMESTAMP]))

def get_ydata(timepoint,ycol):
    return float(timepoint[ycol])

def get_current_time(timestamps):
    return timestamps[-1]

def slide_view_window_incrementally(current_time):
    global window_rightbound
    if current_time > window_rightbound:
        window_rightbound = current_time + VIEW_WINDOW/4
        pyplot.xlim([window_rightbound-VIEW_WINDOW,window_rightbound])

def slide_view_window_continuously(current_time):
    if current_time > VIEW_WINDOW:
        pyplot.xlim([current_time-VIEW_WINDOW,current_time])

def stretch_view_window_continuously(current_time):
    pyplot.xlim([0,current_time])

def stretch_view_window_incrementally(current_time):
    global window_rightbound
    if current_time > window_rightbound:
        window_rightbound = current_time + VIEW_WINDOW/4
        pyplot.xlim([0,window_rightbound])

def get_last_line():
    with open(DATAFILE, "rb") as f:
        f.readline()
        f.seek(-1024,2)             # Jump to one kilobyte before the end of the file (2)
        while f.read(1) != b"\n":    # Until EOL is found...
            f.seek(-2,1)             # ...jump back the read byte plus one more.
        lastline = f.readline()      # Read last line.  
    return lastline.split(',')

def update_data(timepoint):
    if (len(timepoint) == TOTAL_COLUMNS):
        timestamps.append(get_time(timepoint))
        for ycol,yseries in enumerate(ydata):
            yseries.append(get_ydata(timepoint,COLUMN_YDATA[ycol]))
        
def update_plot(xseries,yseries):

    for yline,ydata in enumerate(yseries):
        plotlines[yline].set_xdata(xseries)
        plotlines[yline].set_ydata(ydata)
    
    current_time = get_current_time(timestamps)
    # slide the viewing frame along...
    slide_view_window_incrementally(current_time)
    #slide_view_window_continuously(current_time)
    # ...or, stretch the viewing frame!
    #stretch_view_window_continuously(current_time)
    #stretch_view_window_incrementally(current_time)
    fig1.canvas.draw()   # redraw the canvas
    fig1.canvas.flush_events() # http://bastibe.de/2013-05-30-speeding-up-matplotlib.html
	
        
def lookback_initial():
    global file_position
    
    with open(DATAFILE, "rb") as f:
        try:
            timepoint_delay = -1*(get_time(f.readline().split(','))-get_time(f.readline().split(',')))
            print("\nTime delay between datapoints: " + str(timepoint_delay))
            linesize = sys.getsizeof(f.readline())
            backbytes = int(linesize*VIEW_WINDOW/SECONDS_PER_TIMESTAMP_VAL/timepoint_delay)
            print("\nAttempting to jump back " + str(backbytes) + " bytes...")
            f.seek(backbytes,2)      # Jump `backbytes` before the end of the file (2)
            print("\nWe jumped back to " + str(f.tell()))
        except:
            print("\nCan't look back that far, so we went to the beginning\n")
            f.seek(0,0)
        
        f.readline() # throw away the (probably) partial line you landed in the middle of
        #while f.read(1) != b"\n":   # Until EOL is found...
        #    f.seek(-2,1)            # ...jump back the read byte plus one more.
            
        while True:
            line = f.readline()
            if not line:
                break
            timepoint = line.split(',')
            update_data(timepoint) 
            file_position = f.tell() # advance the file position marker

def data_quality(line):
    datapoint = line.split(',')

    if not line:
        return False
    elif not (len(datapoint) == TOTAL_COLUMNS):
        return False
    elif not line.endswith('\n'):
        return False
    elif ('' in datapoint):
        return False
    else:
        return True

def lookback_update():
    global file_position
    
    with open(DATAFILE, "rb") as f:
        f.seek(file_position,0)
        while True:
            line = f.readline()
            if not line:
                break
            if data_quality(line):   # if the data is quality...
                timepoint = line.split(',')
                update_data(timepoint)
            file_position = f.tell()      # advance the file position marker
        
def main():
    lookback_initial()
    while run:
        lookback_update()
        update_plot(timestamps,ydata)
        sleep(LOOP_DELAY)

main()

