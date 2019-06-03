from __future__ import division
import csv
import sys
import random
import scipy
import numpy
import datetime as datetime
import dateutil.parser
import pandas as pd
from functools import reduce
from collections import OrderedDict
from collections import namedtuple

class ImportData:
    def __init__(self, data_csv,base_name, headings_list):
        self = pd.read_csv(data_csv, sep='\t', skiprows=1, names=headings_list)
        self=self.fillna(method='ffill',axis=0)
        CGM = createDataArrayCGM(self)
        CARB = createDataArrayCarb(self)
        INS = createDataArrayInsulin(self)

        bigData = conCat([CGM,CARB,INS])
        # print("---CGM----")
        # print(CGM)
        # print("---CARB---")
        # print(CARB)
        # print("---INS---")
        # print(INS)
        # print("---all---")
        # print(bigData)

        #save2csv(CGM,base_name+'_cgm')
        save2csv(bigData,base_name+'_all')
