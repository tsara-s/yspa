from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from csv import DictReader

# import image

hdu = fits.open('NGC865_B_918.fit')


# print(hdu.info())

data=hdu[0].data

plt.imshow(data,cmap='gray',vmin=500, vmax=1000)
# plt.show()
# data = data.flatten()

# counts, bins = np.histogram(data)
# print(count)


# plt.hist(data, color = 'r', bins=[0, 3000, 60000])
# plt.colorbar()
plt.show()

npdata = np.int64(data)

center_x = 453
center_y = 356
size = 6

# bgring = npdata[center_x - size-1:center_x+size+2,center_y - size-1:center_y+size+2]
# print(bgring)
# print("\n")
# print(bgring[0])
# print(bgring[-1])
# print(bgring[:,0])
# print(bgring[:,-1])

# bgnoise = np.sum(bgring[0]) + np.sum(bgring[-1]) + np.sum(bgring[:,0]) + np.sum(bgring[:,-1])
# bgnoise -= (bgring[0,0] + bgring[-1,-1] + bgring[0,-1] + bgring[-1,0])
# print((2*(size+1)+1))
# bgnoise /= 4*(2*(size+1)+1)-4
# print(bgnoise)
# print(bgring - bgnoise)

#returns flux, centroid
def flux_centroid(file, center_x, center_y, size):
    hdu = fits.open(file)
    data=hdu[0].data
    
    sliced_arr = npdata[center_y-size : center_y+size+1, center_x-size : center_x+size+1]
    
    bgring = npdata[center_y-size-1 : center_y+size+2, center_x-size-1 : center_x+size+2]
    bgnoise = np.sum(bgring[0]) + np.sum(bgring[-1]) + np.sum(bgring[:,0]) + np.sum(bgring[:,-1])
    bgnoise -= (bgring[0,0] + bgring[-1,-1] + bgring[0,-1] + bgring[-1,0])
    
    #average the bg noise to get mean bg noise
    bgnoise /= 4*(2*(size+1)+1)-4
    

    sliced_arr = sliced_arr-bgnoise
    
    
    
    flux = np.sum(sliced_arr)
    
    x_center = 0
    y_center = 0
     
    # weighted sum of rows and columns
    for i in range(0, len(sliced_arr)):
        x_center += np.sum(sliced_arr[i])*i
        y_center += np.sum(sliced_arr[:,i])*i
    
    
    
    x_center/=flux
    y_center/=flux
       
    centroid = x_center, y_center
    return flux, centroid
    

    
# print(flux_centroid('NGC865_B_918.fit', center_x, center_y, size))


# print(flux_centroid_csv('NGC865_B_918.fit', 'Photometry Coordinates - Sheet2.csv'))


with open('Photometry Coordinates - Sheet2.csv', 'r') as f:
    dict_reader = DictReader(f)
    coordlist = list(dict_reader)

flux_list = []
centroid_list = []

for i in range(0, len(coordlist)):
    x = round(float((coordlist[i]['x'])))
    y = round(float((coordlist[i]['y'])))
    r = round(float((coordlist[i]['radii'])))
    
    flux_list.append(flux_centroid('NGC865_B_918.fit', x, y, r)[0])
    
    centroid_list.append(flux_centroid('NGC865_B_918.fit', x, y, r)[1])
    
print(flux_list)
#     print(centroid_list)