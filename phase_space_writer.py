
import numpy as np 
# This file write BTE.WP3 to new file with space after every phonon mode.
data = np.loadtxt("BTE.WP3")

f=open("separated-BTE.WP3", "w")
nmodes = 60 # system dependent # (no. of atoms * 3)
m,n = np.shape(data)
irr_qpts = 728 # no. of irreproducible qpoints in BZ # get it from BTE.qpoints file.
print(m,n)
count = 0
for i in range(0,m):
    count += 1 

    #f.write(data[i,0], data[i,1], "\n")
    if count %  irr_qpts == 0:
        f.write("{} {} \n".format(data[i,0], data[i,1]))
        f.write("                      "+"\n")
        count = 0
    else:
        f.write("{} {} \n".format(data[i,0], data[i,1]))
