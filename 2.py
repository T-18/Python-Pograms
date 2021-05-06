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
count = 1
chrw = ""
file = open('eg.txt', 'r')
while 1:
	sp = file.read(1)

	if count<= 3:
		chrw = chrw + sp

	if count>3:
		if sp ==" ":
			count = 0
			if len(chrw)>0:
				print(chrw)
				chrw =""
		elif sp !=" ":
			chrw =""
	count = count + 1

	if not sp:
		break

file.close()
