import pydicom
import os
import numpy as np
import cv2

#Image_Path = "C:\\Soumick\\Prostate Classification task\\test2"
Image_Path = "C:\\Soumick\\Prostate Classification task\\2\\test2"

dicom_files_list = []  
for directory, sub_directory, image_list in os.walk(Image_Path):
    #print(directory)
    #print(image_list)
    for image_name in image_list:
        if ".dcm" in image_name.lower():  # check whether the file's DICOM
            dicom_files_list.append(os.path.join(directory,image_name))
            
# Get ref file
sample_ds = pydicom.read_file(dicom_files_list[0])


# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
check_pixel_dim = (int(sample_ds.Rows), int(sample_ds.Columns), len(dicom_files_list))

resize_pixel_dim = (64, 64, len(dicom_files_list))

# Load spacing values (in mm)
check_pixel_spacing = (float(sample_ds.PixelSpacing[0]), float(sample_ds.PixelSpacing[1]), float(sample_ds.SliceThickness))

# The array is sized based on 'check_pixel_dim'
#image_array = np.zeros(check_pixel_dim, dtype=sample_ds.pixel_array.dtype)
image_array = np.zeros(resize_pixel_dim)

# loop through all the DICOM files
get_image_sizes = []
for image in dicom_files_list:
    # read the file
    ds = pydicom.read_file(image)
    get_image_sizes.append([ds.Rows, ds.Columns])
    '''if ds.Rows == check_pixel_dim[0] and ds.Columns == check_pixel_dim[1]:
        
        image_array[:, :, dicom_files_list.index(image)] = ds.pixel_array
    else:
        img = cv2.resize(ds.pixel_array,(check_pixel_dim[0],check_pixel_dim[1]))
        image_array[:, :, dicom_files_list.index(image)] = img
        
    # store the raw image data
   # image_array[:, :, dicom_files_list.index(image)] = ds.pixel_array'''
    img = cv2.resize(ds.pixel_array,(resize_pixel_dim[0], resize_pixel_dim[1]))
    image_array[:, :, dicom_files_list.index(image)] = img
    