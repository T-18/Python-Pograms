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
start = 11
end = 25

for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)