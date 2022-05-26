import numpy as np
import math

def Add(a,b):
    arr = np.array([a,b])
    # np.savetxt("/Desktop/text.txt", arr) # Unable to get this to work
    return a+b;

def find_component_center(arr):
    arr = np.array(arr).reshape(4,3)
    temp = np.average(arr, axis = 0)
    return np.append(temp, (convert_to_polar(arr[2]-arr[0])+convert_to_polar(arr[3]-arr[1]))/2);

def convert_to_polar(xyzArr):
    return math.atan(xyzArr[1]/xyzArr[0]);

