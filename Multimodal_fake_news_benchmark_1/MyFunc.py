
import pandas as pd
import os
import glob
import numpy as np
from PIL import Image
from sklearn.cluster import kmeans_plusplus
from sklearn.cluster import KMeans
import re

def read_benchmark_set(save_path):
 
    tr_sv_path = os.path.join(save_path, 'train_1.csv')
    dev_sv_path = os.path.join(save_path, 'dev1.csv')
    te_sv_path = os.path.join(save_path, 'test1.csv')
    
    tr_df = pd.read_csv(tr_sv_path, header=0, sep=',')
    dev_df = pd.read_csv(dev_sv_path, header=0, sep=',')
    te_df = pd.read_csv(te_sv_path, header=0, sep=',')

    print('Training set has {} fake news and {} true news'.format((tr_df['det_fake_label'] == 1).sum(),
                                                         (tr_df['det_fake_label'] == 0).sum()))
    print('Validation set has {} fake news and {} true news'.format((dev_df['det_fake_label'] == 1).sum(),
                                                         (dev_df['det_fake_label'] == 0).sum()))
    print('Testing set has {} fake news and {} true news'.format((te_df['det_fake_label'] == 1).sum(),
                                                         (te_df['det_fake_label'] == 0).sum()))
    return tr_df, dev_df, te_df
