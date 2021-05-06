#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TANU
#
# Created:     08/02/2021
# Copyright:   (c) TANU 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Using for loop
def Len(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
str = "Tanu"
print(Len(str))