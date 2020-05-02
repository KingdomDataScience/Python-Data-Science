# -*- coding: utf-8 -*-
def plot_dataframe(df, plot_type, x, y, settings):

# dataframe is a Pandas dataframe

# plot_type is a string with the type of plot: ‘scatter’, ‘line’, ‘loglin’, ‘loglog’, ‘linlog’, ‘histogram’, ‘pie’, etc

# x is the name of the Pandas column of the independent variable

# y is a list of names of Pandas columns of the dependent variables

# settings is a dictionary that is specific to each plot type
import pandas as pd
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
import matplotlib

  if plot_type == 'statistics' or plot_type == 'data sample':

    if plot_type == 'statistics':

      print(df.columns.values)

      if len(y) > 0:

        return df[y].describe().to_string()

      else:

        return df.describe().to_string()

  if plot_type == 'data sample':

    print(df.columns.values)

    if len(y) > 0:

      return df[y].head(10).to_string()

    else:

      return df.head(10).to_string()                                  

  else:

    if x == '-Index-':

      x = range(0, len(df))

    else:

      x = df[x].values

    if plot_type == 'line':

      #x = df[x].values

      y = df[y].values

      print(x[0:5])

      print(y[0:5])

      plt.plot(x, y)

    if plot_type == 'scatter':

      print(x)

     #x = df[x].values

      y = df[y].values

      plt.scatter(x, y)

    if plot_type == 'histogram':

      #x = df[x].values

      n, bins, patches = plt.hist(x, bins=10)

      print(len(bins))

    if 'graphTitle' in settings:

      plt.title(settings['graphTitle'])

    if 'xAxisLabel' in settings:

      plt.xlabel(settings['xAxisLabel'])

    if 'yAxisLabel' in settings:

      plt.ylabel(settings['yAxisLabel'])              

    if plot_type != 'histogram' and 'showLegend' in settings and settings['showLegend'] == True:

      plt.legend(settings['DependentVariable'])

    f = io.BytesIO()

    plt.savefig(f, format="png", facecolor=(0.95,0.95,0.95))

    plt.clf()

  return f