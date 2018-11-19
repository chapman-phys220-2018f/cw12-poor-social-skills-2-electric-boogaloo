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
import sombrero as sb

def test_sombrero():
    """
    Checks if the first 3 and last 3 values of a known function are correct.
    """
    knownStartx = np.array([-0.9, -0.9, -0.89999998])
    knownStarty = np.array([0.00000000e+00, 8.99884295e-06, 1.79952436e-05])
    knownEndx = np.array([-0.81623219, -0.81619339, -0.8161547 ])
    knownEndy = np.array([0.03885052, 0.03874837, 0.03864621])
    testVals = sb.sombrero(0.18, -0.9, 0, 50)
    assert np.allclose(testVals[0,0:3], knownStartx) and np.allclose(testVals[1,0:3], knownStarty) and np.allclose(testVals[0,-4:-1], knownEndx) and np.allclose(testVals[1,-4:-1], knownEndy)