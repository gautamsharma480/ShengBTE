import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import interp1d

data = np.loadtxt("kappa.dat")

'''npts = 200

x_new = np.linspace(data[1,0],data[-1,0],npts)

#interpolated_data = np.interp(x_new, data[:,0],data[:,1])
interpolated_data = interp1d(data[:,0],data[:,1],kind='cubic')
#interpolated_data = interp1d(data[:,0],data[:,1],kind=3)

print(np.shape(interpolated_data))
interpolated_data_sp = interpolated_data(x_new)

intp_data = np.empty((npts,npts))

for i in range(0,npts):
    #adding 1d data into 2d "data" array
    intp_data[i,0] = np.array(x_new[i])
    intp_data[i,1] = np.array(interpolated_data_sp[i])

'''

def central_difference(data):
    # this function is for original data (input data has 5 columns)
    f=open("spectral_kappa.dat","w")
    rg = np.shape(data)[0]
    print(rg)
    sigma=1
    df = np.zeros((rg,1))
    dx = data[1,0]-data[0,0]
    for i in range(1, rg-1):
        df[i] = (data[i+1,1] - data[i-1,1])/(2*dx)
        #kappa[i] = gaussian_filter1d(df[:], sigma, order=0)
        f.write(str(data[i,0])+"  "+str(df[i,0])+"\n")
       
    #kappa = gaussian_filter1d(df, sigma, order=0)
    plt.plot(data[:,0],df)
    #plt.plot(kappa)
    
    #plt.show()

def forward_difference(data):
    # this function is for original data (input data has 5 columns)
    f=open("spectral_kappa_fd.dat","w")
    rg = np.shape(data)[0]
    print(rg)
    df = np.zeros((rg,1))
    dx = data[1,0]-data[0,0]
    for i in range(0, rg-1):
        df[i] = (data[i+1,1] - data[i,1])/dx
        f.write(str(data[i,0])+"  "+str(df[i,0])+"\n")

    plt.plot(data[:,0],df)


central_difference(data)
forward_difference(data)
#forward_difference(intp_data)
#central_difference(intp_data)
plt.show()
#forward_difference(data)
