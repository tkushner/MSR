from __future__ import division
import csv
import sys
import math
import scipy
import scipy.stats as spStats
import statistics as stats
import numpy as np
import datetime as datetime
import dateutil.parser
import pandas as pd
from functools import reduce
from collections import OrderedDict
from collections import namedtuple

class talkLife:
    def __init__(self,data_csv,base_name):
        self = pd.read_csv(data_csv)
        #self=self.fillna(method='ffill',axis=0)

        #bigFrame = splitPosts(self,base_name)
        #stdFrame = standardize(bigFrame)
        #bigData = conCat([CGM,CARB,INS])

        #save2csv(bigData,base_name+'_all')

        #splitTZ = splitTimeZones(self)
        #save2csv(splitTZ,base_name)

        save2csv(self[['QiD','TDiff','QLocTZ','ALocTZ','DiffTZ']].set_index('QiD'),'TZdata_raw')

def splitPosts(dataFrame,base_name):
    bigFrame = pd.DataFrame(columns=["_date"])
    _first = True
    for Idx in dataFrame.NewMood_dailyMean.unique():
        _newFrame = dataFrame.loc[dataFrame["NewMood_dailyMean"]==Idx,:]
        _idxStr = str(Idx)

        if _idxStr != 'nan':
            _newFrame = _newFrame.rename(columns={'NumPosts':_idxStr})
            _newFrame = _newFrame.set_index('_date')
            _newFrame = _newFrame.drop(columns={'NewMood_dailyMean'})
            if _first:
                bigFrame = _newFrame
                _first = False
            else:
                bigFrame = pd.concat([bigFrame, _newFrame], axis=1, sort=True)

    bigFrame.fillna(value=0,inplace=True)
    return bigFrame

def splitTimeZones(df):
    #gets stats post-by-post
    tzStats = pd.DataFrame(columns=["QiD","maxDiff","minDiff","modeDiff","stdDiff","meanDiff","OGtz","MeanTSincePost","MaxTSincePost","MinTSincePost"])
    for Idx in df.QiD.unique():
        tzValues = df.loc[df['QiD']==Idx,'DiffTZ'].values
        maxDiff = max(tzValues)
        minDiff = min(tzValues)

        if minDiff == maxDiff:
            stdDiff = 0
            modeDiff = minDiff
            meanDiff = 0
        else:
            stdDiff = stats.stdev(tzValues)
            modeDiff = spStats.mode(tzValues)[0]
            meanDiff = stats.mean(tzValues)

        OGtz = stats.mean(df.loc[df['QiD']==Idx,'QLocTZ'].values)

        tSincePost = df.loc[df['QiD']==Idx,'TDiff'].values
        MeanTSincePost = stats.mean(tSincePost)
        MinTSincePost = min(tSincePost)
        MaxTSincePost = max(tSincePost)

        newData={"QiD":[Idx],"maxDiff":[maxDiff],"minDiff":[minDiff],"meanDiff":[meanDiff],"modeDiff":[modeDiff],"stdDiff":[stdDiff],"OGtz":[OGtz],"MeanTSincePost":[MeanTSincePost],"MinTSincePost":[MinTSincePost],"MaxTSincePost":[MaxTSincePost]}
        newVal = pd.DataFrame(newData).set_index("QiD", drop=False)
        newVal = newVal.astype('float64')
        tzStats=tzStats.append(newVal,sort=True)

    print(tzStats.modeDiff)
    return(tzStats)

def standardize(dataFrame):
    stdFrame = dataFrame
    stdFrame['totalPosts'] = dataFrame.sum(axis=1)
    stdFrame = stdFrame.div(stdFrame.totalPosts, axis=0)
    return stdFrame

def save2csv(dataFrame,file_name):
    dataFrame.to_csv (file_name+'.csv', index = True, header=True)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Useage:',sys.argv[0],'[data_file_name] [base_name]')
        sys.exit(2)

    file_name = sys.argv[1]
    base_name = sys.argv[2]

    # with open(heading_file,'r') as csvfile:
    #     headings = []
    #     for item in csvfile:
    #         headings.append(item.rstrip()) #rstrip removes the newline character
    #     csvfile.close()
    # print(headings)


    Data = talkLife(file_name,base_name)
