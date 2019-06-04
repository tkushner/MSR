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

class talkLife:
    def __init__(self, headings_list, data_csv,base_name):
        self = pd.read_csv(data_csv, header=None, names=headings_list)
        self=self.fillna(method='ffill',axis=0)

        print(self)
        #bigData = conCat([CGM,CARB,INS])

        #save2csv(bigData,base_name+'_all')

def pullTimeZones(dataFrame):
    

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Useage:',sys.argv[0],'[heading_file_name] [data_file_name] [base_name]')
        sys.exit(2)

    heading_file = sys.argv[1]
    file_name = sys.argv[2]
    base_name = sys.argv[3]

    with open(heading_file,'r') as csvfile:
        headings = []
        for item in csvfile:
            headings.append(item.rstrip()) #rstrip removes the newline character
        csvfile.close()
    print(headings)


    Data = talkLife(headings,file_name,base_name)
