import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from astroquery.esasky import ESASky

print(ESASky.list_maps())

maps = ESASky.query_object_maps('M51')
print(maps)

print(maps['XMM-OM-OPTICAL'].info)
maps['XMM-OM-OPTICAL']['observation_id', 'instrument', 'filter', 'duration'].pprint()

print('Downloading maps to /home/kiffles/Workspaces/Python/ESAscript/ ')
maps_data = ESASky.get_maps(maps, 'XMM-OM-OPTICAL', download_dir = '/home/kiffles/Workspaces/Python/ESAscript/')

print('These are all the images: ', maps_data)

print('here is one image')

hdu = maps_data['XMM-OM-OPTICAL'][2]

print('This is the header for this image:', hdu[0].header)

image = hdu[0].data 

plt.show(plt.colorbar(plt.imshow(image, norm = LogNorm(), cmap='gray')))

exit()

