import numpy as np
import pandas as pd


def f2c_matrix(params):
    a, b, c, v = params['a'], params['b'], params['c'], params['volume']
    calp = np.cos(np.radians(params['alpha']))
    cbet = np.cos(np.radians(params['beta']))
    cgam = np.cos(np.radians(params['gamma']))
    sgam = np.sin(np.radians(params['gamma']))
    r1 = (a, -(b * cgam), c * cbet)
    r2 = (0, b*sgam, c*((calp-cbet*cgam)/sgam))
    r3 = (0, 0, v/(a*b*sgam))
    matrix = pd.DataFrame([r1, r2, r3], columns=['x', 'y', 'z'])
    return matrix


def c2f_matrix(params):
    a, b, c, v = params['a'], params['b'], params['c'], params['volume']
    calp = np.cos(np.radians(params['alpha']))
    cbet = np.cos(np.radians(params['beta']))
    cgam = np.cos(np.radians(params['gamma']))
    sgam = np.sin(np.radians(params['gamma']))
    r1 = (1 / a, -(cgam / (a * sgam)), b * c * ((calp * cgam - cbet) / (v * sgam)))
    r2 = (0, 1/(b*sgam), a*c*((cbet*cgam-calp)/(v*sgam)))
    r3 = (0, 0, (a*b*sgam)/v)
    matrix = pd.DataFrame([r1, r2, r3], columns=['x', 'y', 'z'])
    return matrix


def coord_convert(points, params, order):
    if order == 0:
        matrix = c2f_matrix(params)
    else:
        matrix = f2c_matrix(params)
    converted = []
    for i in range(0, len(points)):
        v = np.array(points.loc[i, 'x':'z'])
        converted.append((np.dot(matrix, v)[0],
                          np.dot(matrix, v)[1],
                          np.dot(matrix, v)[2]))
    converted = pd.DataFrame(converted, columns=['x', 'y', 'z'])
    return converted
