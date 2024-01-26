
import numpy as np 
# This file write BTE.WP3 to new file with space after every phonon mode.
data = np.loadtxt("BTE.WP3")

f=open("separated-BTE.WP3", "w")
nmodes = 60
m,n = np.shape(data)
irr_qpts = 728
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
