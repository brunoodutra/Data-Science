# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:41:29 2021

@author: Bruno Dutra
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px


def analyze(csv_file):
    datalog=pd.read_csv(csv_file,';')
    # drop all rows with any NaN and NaT values
    datalog = datalog.dropna()
    
    GDP=datalog['GDP - per capita']
    x=pd.to_numeric(GDP[1:], errors='coerce')
    
    file_exp=datalog["Life expectancy at birth(years)"]
    y=pd.to_numeric(file_exp[1:], errors='coerce')
    
    #%% Like a boss 
    phi= np.array([x, np.ones(len(x))]).T
    
    theta= np.linalg.inv(phi.T.dot(phi)).dot(phi.T).dot(y)
    y_est= phi.dot(theta)
    #%% Results
    fig, ax = plt.subplots()
    ax.plot(x,y_est)
    ax.plot(x,y,'.')
    ax.set_xlabel("GDP - per capita")
    ax.set_ylabel("Life expectancy at birth(years)")
    plt.show()

analyze('factbook.csv')