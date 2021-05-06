#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TANU
#
# Created:     06/02/2021
# Copyright:   (c) TANU 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
def squaresum(n) :
    sum = 0
    for i in range(1, n+1) :
        sum = sum + (i * i)
    return sum
n = 5
print(squaresum(n))