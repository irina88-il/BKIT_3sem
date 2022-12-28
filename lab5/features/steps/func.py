import math
def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        y = -b / (2.0*a)
        if y >= 0:
            root_1 = math.sqrt(y)
            root_2 = -math.sqrt(y)
            result.append(root_1)
            result.append(root_2)      
    elif D > 0.0:
        sqD = math.sqrt(D)
        y1 = (-b + sqD) / (2.0*a)
        y2 = (-b - sqD) / (2.0*a)
        if (y1 >= 0):
            root1_1 = math.sqrt(y1)
            root1_2 = -math.sqrt(y1)
            result.append(root1_1)
            result.append(root1_2)
        if (y2 >= 0):
            root2_1 = math.sqrt(y2)
            root2_2 = -math.sqrt(y2)
            result.append(root2_1)
            result.append(root2_2)
    return result
