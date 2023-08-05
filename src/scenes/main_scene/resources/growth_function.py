import math

def growth(x, max, smoothness):
    return max / (1 + max * math.pow(math.e, -(x / smoothness)))