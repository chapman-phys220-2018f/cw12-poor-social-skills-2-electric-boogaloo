#! /usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Trevor Kling
# Student ID: 0022707716
# Email: kling109@mail.chapman.edu
# Course: PHYS/CPSC/MATH 220 Fall 2018
# Assignment: CW 12
###

import numpy as np

def sombrero(F, x0, y0, N):
    """
    Returns a data set corresponding to a time range for a sombrero function.  Uses a matrix to find the derivatives:
    Parameters:
    -----------
    F: Float
        Represents a constant used in the formula for the driving force
    x0: Float
        The initial value for x
    y0: Float
        The initial value for y
    N: int > 0
        An integer which denotes the upper limit of the range of t values.

    Returns:
    --------
    brero: np.array([float, float])
        An array of values for various values of the sombrero function at different time values. The values are returned as pairs, [x(t), y(t)].
    """
    delT = 0.001
    tRange = np.arange(0, 2*np.pi*N, delT)
    brero = np.zeros((len(tRange)+1, 2))
    brero[0] = np.array([x0, y0])
    n = 1
    def derivative(t, r, F):
        """
        Produces the derivative.  r is an array of [x, y].
        """
        dF = np.array([r[1], -0.25*r[1] + r[0] - r[0]**3 + F*np.cos(t)])
        return dF
    for n in range(len(tRange)):
        k1 = delT*(derivative(tRange[n], brero[n], F))
        k2 = delT*(derivative(tRange[n] + delT/2, brero[n] + (k1/2), F))
        k3 = delT*(derivative(tRange[n] + delT/2, brero[n]+ (k2/2), F))
        k4 = delT*(derivative(tRange[n] + delT, brero[n] + k3, F))
        brero[n+1] = brero[n] + ((k1 + 2*k2 + 2*k3 + k4)/6)
    return np.array([brero[:,0], brero[:,1]])