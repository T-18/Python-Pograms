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
# using while loop.
def Len(string):
    counter = 0
    while string[counter:]:
        counter += 1
    return counter
string = "T"
print(Len(string))