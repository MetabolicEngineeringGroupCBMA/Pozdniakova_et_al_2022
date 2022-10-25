#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pydna.utils import parse_text_table

data = """\
Time (h)	OD600
0.000	    0.1000
13.183	    0.1620
15.917	    0.2800
18.000	    0.4600
19.833	    0.5600
21.750	    0.6200
23.750	    0.8000
27.500	    1.1800
32.750	    2.0200
41.500	    4.7200
44.167	    5.7200
48.833	    6.0400
53.283	    5.9600
"""
*r, cr = parse_text_table(data)

# Data input
xData = np.array(cr[0][1:], dtype="f")
yData = np.array(cr[1][1:], dtype="f")

xData

yData

np.e


def mgomb(t, A, Tlag, µm):
    """
    Gompertz (Tjørve 2017).

    A = upper asymptote
    t = time
    µm = growth-rate coefficient
    Tlag =
    """
    return A*np.exp(-np.exp((np.e*µm/A)*(Tlag-t)+1))


#     # =$C$18+$D$11*EXP(-EXP(($D$12*EXP(1))/$D$11*($D$13-B19)+1))
#
#     # = c + A*EXP(-EXP( ($D$12*EXP(1))/$D$11*($D$13-B19)+1 ))
#
#     =$C$18+$D$11*EXP(-EXP(($D$12*EXP(1))/$D$11*($D$13-B19)+1))
#
#
#     =$C$18+$D$11*EXP(-EXP((($D$12*EXP(1))/$D$11)*($D$13-B30)+1))
#
#
#     = constant + A * EXP(-EXP(((µm *EXP(1))/$D$11)*($D$13-B30)+1))

# curve fit the test data
fittedParameters, pcov = curve_fit(mgomb, 
                                   xData, 
                                   yData,
                                   bounds=([0.01, 20.0, 0.01], [8.0, 25.0, 1.0]))

A, Tlag, µm = fittedParameters

A, Tlag, µm

fig, ax = plt.subplots()
ax.plot(xData, yData, "^")
t = np.arange(min(xData), max(xData), 0.01)
ax.plot(t, mgomb(t, A, Tlag, µm))
plt.show()


def exp_growth(t, x0, µmax):
    # x0 initial optical density
    # t = time (h)
    # µmax maximum growth rate (1/h)
    return x0 * np.exp(µmax * t)


first_data_point = 8

number_of_datapoints = 3

xSelection = xData[first_data_point:first_data_point+number_of_datapoints]

ySelection = yData[first_data_point:first_data_point+number_of_datapoints]

fittedParameters, pcov = curve_fit(exp_growth, 
                                   xSelection,
                                   ySelection,
                                   bounds=([0.0, 0.0], [1.0, 1.0]))

x0, µmax = fittedParameters

x0

µmax

fig, ax = plt.subplots()
ax.plot(xData, yData, "^")
t = np.arange(min(xData), max(xData), 0.01)
ax.plot(t, mgomb(t, A, Tlag, µm))
ax.plot(t, exp_growth(t, x0, µmax))
plt.show()


def gomb(t, A, Ti, kg):
    """
    Gompertz (Tjørve 2017).

    A = upper asymptote
    t = time
    kg = growth-rate coefficient
    Ti = time at inflection
    """
    return A*np.exp(-np.exp(-kg*(t-Ti)))
# curve fit the test data
fittedParameters, pcov = curve_fit(gomb, 
                                   xData, 
                                   yData,
                                   bounds=([0.01, 0.01, 0.01], [7.0, 50.0, 1.0]))

A, Ti, kg = fittedParameters

A

Ti

kg

fig, ax = plt.subplots()
ax.plot(xData, yData, "^")
t = np.arange(min(xData), max(xData), 0.01)
ax.plot(t, mgomb(t, A, Tlag, µm))
ax.plot(t, exp_growth(t, x0, µmax))
ax.plot(t, gomb(t, A, Ti, kg))
plt.show()


