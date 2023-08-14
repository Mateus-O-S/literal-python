import math

def get_sin_cos(a, b):
    xdis = a[0] - b[0] 
    ydis = a[1] - b[1]
    dis = math.sqrt(xdis * xdis + ydis * ydis)
    if dis != 0:
        return [xdis / dis, ydis / dis]
    return [0, 0]