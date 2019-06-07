# Author(s): Haley Acevedo
import json
import numpy as np
import pandas as pd
import re

from os import listdir

x_interp = np.arange(0, 90, .6)
x_data = np.arange(0, 90, .25)

def create_df(rows, label):
    column_names = ['subject', 'trial'] + [ 'frame' + str(x) for x in range(1, len(rows[0])-1) ]
    df = pd.DataFrame(rows, columns=column_names).set_index(['subject', 'trial']).sort_index()
    df.to_csv('{}_discomfort_trials.csv'.format(label))
    return df


def interpolate_data(y):
    return [ str(x) for x in np.interp(x_interp, x_data, y).tolist() ]


def write_fidl_file(row):
    fidl_file = '{}_avg_discomfort.ext'.format(row.name)
    avg_trial = [ str(x) for x in list(row.values) ]
    with open(fidl_file, 'w') as f:
        run_discomfort = [avg_trial[0]] *50 + avg_trial*4 # initial 30s rest (with initial value of discomfort curve) + 4 concatenated discomfort curves
        f.write('\n'.join(['discomfort'] + run_discomfort*2)) # write label and two runs worth of discomfort curves
    return row


blink_trials = { re.search('(ResampledBlinks(TM\d{3})_Trial(\d)OK.txt)', f) for f in listdir('.') }
blink_trials = { x.groups() for x in blink_trials if x }

orig_rows = []
eye_closure_rows = []
resamp_rows = []
for trial_info in blink_trials:
    y = np.genfromtxt(trial_info[0], usecols=1)
    y_resamp = interpolate_data(y)
    index_cols = [trial_info[1], trial_info[2]]
    orig_rows.append(index_cols + list(y))
    eye_closure_rows.append(index_cols + list(np.genfromtxt(trial_info[0], usecols=3)))
    resamp_rows.append(index_cols + y_resamp)

resamp_df = create_df(resamp_rows, 'resampled')
orig_df = create_df(orig_rows, 'original')
eye_closure_rows = create_df(eye_closure_rows, 'eye_closure')

frame_cols = [col for col in resamp_df.columns if col.startswith('frame')]
resamp_df[frame_cols] = resamp_df[frame_cols].astype(float)
avg_df = resamp_df.groupby('subject')[frame_cols].mean()
avg_df.to_csv('average_dicomfort_curves.csv')
avg_df.apply(write_fidl_file, axis=1)
