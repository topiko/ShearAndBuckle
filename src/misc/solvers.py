'''
Created on 17.8.2015

@author: tohekorh
'''
import numpy as np
from scipy.optimize import fmin

def get_R(L, deltaY):
    
    g = lambda R: (deltaY + R * np.cos(L / R) - R)**2 
    
    if deltaY != 0:
        return fmin(g, L**2 / 2 * deltaY, disp = 0)[0]

    else: return 0


def int_toAngst(thatInt, edge, key = 'width', C_C = 1.42):
    
    if edge == 'zz':
        if key == 'width':
            return thatInt * 3. / 2 * C_C - C_C
        if key == 'length':
            return (thatInt - 1) * np.sqrt(3) / 2 * C_C 
    
    if edge == 'ac':
        if key == 'width':
            return (thatInt -1) * np.sqrt(3) * C_C / 2. 
        if key == 'length':
            return thatInt * 3. / 2 * C_C - C_C 
    
    