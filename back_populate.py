#!/opt/anaconda/envs/infrasound/bin/python
# -*- coding: utf-8 -*-
"""
Created on 24-Apr-2018
@author: awech
"""

import pandas as pd
import os

T1='2018-10-05 00:00'
T2='2018-10-05 17:30'

for t in pd.date_range(T1, T2, freq='10min'):
	os.system('./array_processing.py {}'.format(t.strftime('%Y%m%d%H%M')))
