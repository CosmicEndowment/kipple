from astropy.io import fits
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Handle FITS extract image data to numpy array

data, header = fits.getdata("ZWO.fits", header=True)
my_FITS = fits.open("ZWO.fits")
my_FITS.info()
data = my_FITS[0].data
my_FITS.close()

# plot channel in matplotlib and color range

plt.show(plt.colorbar((plt.imshow(data, cmap='gray'))))

# Export three fits images

fits.writeto('ZWO_output.fits', data, header, overwrite=True)

exit()

