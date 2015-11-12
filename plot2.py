import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np    

# Converter function
datefunc = lambda x: mdates.date2num(datetime.strptime(x, '%d/%m'))

# Read data from 'file.dat'
date, time, high, low, bpm = np.genfromtxt('readings2.dat',    # Data to be read
                                           delimiter=5,  # First column is 19 characters wide
                                           converters={0: datefunc}, # Formatting of column 0
                                           dtype=float,   # All values are floats
                                           unpack=True)   # Unpack to several variables

fig = plt.figure()
ax = fig.add_subplot(111)

# Configure x-ticks
ax.set_xticks(dates) # Tickmark + label at every plotted point
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))

ax.plot_date(dates, levels, ls='-', marker='o')
ax.set_title('title')
ax.set_ylabel('Waterlevel (m)')
ax.grid(True)

# Format the x-axis for dates (label formatting, rotation)
fig.autofmt_xdate(rotation=45)
fig.tight_layout()

fig.show()
