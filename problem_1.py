def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0: 
        return -1
    L = 1
    R = number
    while True:
        M = int((L + R) / 2)
        sq = M * M
        if sq == number:
            return M
        elif sq < number:
            M2 = M + 1
            sq2 = M2 * M2
            if sq2 > number:
                return M
            L = M
        elif sq > number:
            R = M


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (-1 == sqrt(-2)) else "Fail")
print ("Pass" if  (239851 == sqrt(57528502201)) else "Fail")
print ("Pass" if  (2810470 == sqrt(7898745698877)) else "Fail")
