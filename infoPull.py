from __future__ import division
import csv
import sys
import math
import scipy
import numpy as np
import datetime as datetime
import dateutil.parser
import pandas as pd
from functools import reduce
from collections import OrderedDict
from collections import namedtuple

#bokeh
from bokeh.core.properties import field
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import (ColumnDataSource, HoverTool, SingleIntervalTicker,
                          Slider, Button, Label, CategoricalColorMapper)
from bokeh.palettes import Spectral6
from bokeh.plotting import figure

#NLP
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec

class talkLife:
    def __init__(self,data_csv,base_name):
        self = pd.read_csv(data_csv)
        #self=self.fillna(method='ffill',axis=0)

        bigFrame = splitPosts(self,base_name)
        plotBokeh(bigFrame)
        stdFrame = standardize(bigFrame)
        #bigData = conCat([CGM,CARB,INS])

        #save2csv(bigData,base_name+'_all')

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

def standardize(dataFrame):
    stdFrame = dataFrame
    stdFrame['totalPosts'] = dataFrame.sum(axis=1)
    stdFrame = stdFrame.div(stdFrame.totalPosts, axis=0)
    return stdFrame

def save2csv(dataFrame,file_name):
    dataFrame.to_csv (file_name+'.csv', index = True, header=True)

def plotBokeh(dataFrame):
    #x = dataFrame.index.values
    y_dat = dataFrame.iloc[0,:].values
    x_dat = np.linspace(1,len(y_dat),num=len(y_dat))


    N = len(x_dat)

    colors = ["#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(x_dat, y_dat)]

    source = ColumnDataSource(data=dict(xVals=x_dat,
                                    yVals=y_dat,
                                    radii=y_dat*0.5,
                                    moods=dataFrame.columns.values, color=bp.viridis(N)))


    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

    p = figure(tools=TOOLS)

    p.scatter(x='xVals', y='yVals', radius='radii', source=source,
              fill_color='color', fill_alpha=0.6,
              line_color=None)

    labels = LabelSet(x='xVals', y='yVals', text='moods', level='glyph',
              x_offset=5, y_offset=5, source=source)
    p.add_layout(labels)
    output_file("color_scatter.html", title="color_scatter.py example")

    show(p)

def plotBokeh_2(data):

    source = ColumnDataSource(data=data[years[0]])

    plot = figure(x_range=(1, 9), y_range=(20, 100), title='Gapminder Data', plot_height=300)
    plot.xaxis.ticker = SingleIntervalTicker(interval=1)
    plot.xaxis.axis_label = "Children per woman (total fertility)"
    plot.yaxis.ticker = SingleIntervalTicker(interval=20)
    plot.yaxis.axis_label = "Life expectancy at birth (years)"

    label = Label(x=1.1, y=18, text=str(years[0]), text_font_size='70pt', text_color='#eeeeee')
    plot.add_layout(label)

    color_mapper = CategoricalColorMapper(palette=Spectral6, factors=regions_list)
    plot.circle(
        x='fertility',
        y='life',
        size='population',
        source=source,
        fill_color={'field': 'region', 'transform': color_mapper},
        fill_alpha=0.8,
        line_color='#7c7e71',
        line_width=0.5,
        line_alpha=0.5,
        legend=field('region'),
    )
    plot.add_tools(HoverTool(tooltips="@Country", show_arrow=False, point_policy='follow_mouse'))


    def animate_update():
        year = slider.value + 1
        if year > years[-1]:
            year = years[0]
        slider.value = year


    def slider_update(attrname, old, new):
        year = slider.value
        label.text = str(year)
        source.data = data[year]

    slider = Slider(start=years[0], end=years[-1], value=years[0], step=1, title="Year")
    slider.on_change('value', slider_update)

    callback_id = None

    def animate():
        global callback_id
        if button.label == '► Play':
            button.label = '❚❚ Pause'
            callback_id = curdoc().add_periodic_callback(animate_update, 200)
        else:
            button.label = '► Play'
            curdoc().remove_periodic_callback(callback_id)

    button = Button(label='► Play', width=60)
    button.on_click(animate)

    layout = layout([
        [plot],
        [slider, button],
    ], sizing_mode='scale_width')

    curdoc().add_root(layout)
    curdoc().title = "Gapminder"

def wordSim(listWords):
    warnings.filterwarnings(action = 'ignore')


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
