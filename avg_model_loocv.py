import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid

def loocv(group):
    print(group.name)

    trials = group.values
    r_vals = []
    for i in range(5):
        print('Trial {} left out'.format(i))
        incl_trials = [ x for x in range(5) if x != i ]
        actual_disc = trials[i]
        modeled_disc = np.mean(trials[incl_trials, :], axis=0)

        r = np.corrcoef(actual_disc, modeled_disc)[0,1]
        r_vals.append(r)

        #plot(range(360), actual_disc, label='Actual Discomfort')
        #plot(range(360), modeled_disc, label='Modeled Discomfort')
        #plt.legend(bbox_to_anchor=(1.05, .8), loc=2, borderaxespad=0.)
        #plt.show()
    group['corr'] = r_vals
    return group

df = pd.read_csv('original_discomfort_trials.csv', index_col=[0,1])
df = df.groupby('subject').apply(loocv)

df = df.unstack()
df['avg_corr'] = df['corr'].mean(axis=1)
df[['corr', 'avg_corr']].to_csv('avg_method_loocv_results.csv')
