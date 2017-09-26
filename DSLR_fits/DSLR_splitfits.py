
# This file comes with NO warranty and WITHOUT any guarantee of reliability
# or servicability of any kind in any device for any use.

from astropy.io import fits
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Image data to numpy array

data, header = fits.getdata("test.fits", header=True)
my_FITS = fits.open("test.fits")
my_FITS.info() #print FITS info to console
data = my_FITS[0].data
my_FITS.close()
print('Data is type: ', type(data))
print('Dimensions', data.shape)

# Create RGB channels

print('Creating temporary blank 2D arrays for image extraction from PRIMARY')
R = np.zeros((4752,3168))
print('Red channel [0] image dimensions: ', R.shape)
G = np.zeros((4752,3168))
print('Green channel [1] image dimensions: ', G.shape)
B = np.zeros((4752,3168))
print('Blue channel [2] image dimensions: ', B.shape)

#copy channel data from fits

for i in range(0,4752): #RED
	for j in range(0,3168):
		R[i,j] = data[0,j,i]
print('RED done')
		
for i in range(0,4752): #GREEN
	for j in range(0,3168):
		G[i,j] = data[1,j,i]
print('GREEN done')
		
for i in range(0,4752): #BLUE
	for j in range(0,3168):
		B[i,j] = data[2,j,i]
print('BLUE done')

# plot channels in matplotlib for rudimentary debugging

#plt.show(plt.colorbar(plt.imshow(R, cmap='gray')))
#plt.show(plt.colorbar(plt.imshow(G, cmap='gray')))
#plt.show(plt.colorbar(plt.imshow(B, cmap='gray')))

# Export three fits images

fits.writeto('red_channel.fits', R, header, overwrite=True)
fits.writeto('green_channel.fits', G, header, overwrite=True)
fits.writeto('blue_channel.fits', B, header, overwrite=True)

exit()






