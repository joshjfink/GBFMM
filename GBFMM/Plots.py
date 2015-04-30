# ------- #
# Plotting #
# ------- #
from ggplot import *
import pandas as pd

# 
def plot_traj(outs):
    if len(outs) == 2:
        d = {'one' : outs[0], 
        'two' : outs[1], 
        'Time': range(1,len(outs[0])+1)}
    elif len(outs) == 3:
	    d = {'one' : outs[0], 
	    'two' : outs[1], 
	    'three' : outs[2], 
	    'Time': range(1,len(outs[0])+1)}
    elif len(outs) == 4: 
    	d = {'one' : outs[0], 
    	'two' : outs[1], 
    	'three' : outs[2], 
    	'four' : outs[3], 
    	'Time': range(1,len(outs[0])+1)}
    elif len(outs) == 5:
    	d = {'one' : outs[0], 
    	'two' : outs[1], 
    	'three' : outs[2], 
    	'four' : outs[3], 
    	'five' : outs[4], 
    	'Time': range(1,len(outs[0])+1)}
    elif len(outs) == 6:
    	d = {'one' : outs[0], 
    	'two' : outs[1], 
    	'three' : outs[2], 
    	'four' : outs[3], 
    	'five' : outs[4], 
    	'six' : outs[5], 
    	'Time': range(1,len(outs[0])+1)}
    elif len(outs) == 7: 
    	d = {'one' : outs[0],
    	'two' : outs[1], 
    	'three' : outs[2], 
    	'four' : outs[3], 
    	'five' : outs[4], 
    	'six' : outs[5], 
    	'seven' : outs[6], 
    	'Time': range(1,len(outs[0])+1)}
    elif len(outs) == 8:
    	d = {'one' : outs[0],
    	'two' : outs[1], 
    	'three' : outs[2], 
    	'four' : outs[3], 
    	'five' : outs[4], 
    	'six' : outs[5], 
    	'seven' : outs[6], 
    	'eight' : outs[7], 
    	'Time': range(1,len(outs[0])+1)}
    dat = pd.DataFrame(d) 
    dm = pd.melt(dat, id_vars=['Time'], var_name='Latent Class', value_name='Value') 
    print ggplot(dm, aes('Time', 'Value', color='Latent Class')) + \
    	geom_point(size=80) + \
    	geom_line(size=3) + \
    	theme_bw()