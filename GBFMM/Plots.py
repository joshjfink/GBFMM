# ------- #
# Plotting #
# ------- #
from ggplot import *
# 
def plot_traj(outs):
    d = {'one' : outs[0],
     'two' : outs[1],
     'time': range(1,7)}
    dat = pd.DataFrame(d)
    dm = pd.melt(dat, id_vars=['time'])
    print ggplot(dm, aes('time', 'value', color='variable')) + \
        geom_point(size=40) + \
        geom_line(size=3) + \
        theme_bw()