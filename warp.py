import numpy as np
import math

def warp(img, x=0, y=0, f=100):
    """
    This function implements a spherical projection image warping algorithm.
    
    Parameters:
    img (numpy array): The input image.
    x (int): The x offset. Default is 0.
    y (int): The y offset. Default is 0.
    f (int): The focal length. Default is 100.

    Returns:
    numpy array: The warped image.
    numpy array: The warped image cropped to the original image size.
    """
    
    # Initialize the projection plane
    proj_plane = np.zeros((224+abs(x), 224+abs(y), 3), dtype = np.uint8)
    
    # Calculate the center of the image
    x_mid = img.shape[0]/2
    y_mid = img.shape[1]/2
    
    # Iterate over each pixel in the image
    for pix_i in range(img.shape[0]):
        for pix_j in range(img.shape[1]):
            
            # Calculate the angles theta and phi
            theta = math.atan(np.sqrt(abs(x-x_mid+pix_i)**2 + abs(y-y_mid+pix_j)**2)/f)
            phi = math.pi/2 if x-x_mid+pix_i == 0 else math.atan((y-y_mid+pix_j)/(x-x_mid+pix_i))
            
            # Calculate the radius
            r = f * theta
            
            # Calculate the new location of the pixel
            proj_x = int(proj_plane.shape[0]/2 + r*math.cos(phi)) if x-x_mid+pix_i >= 0 else int(proj_plane.shape[0]/2 - r*math.cos(phi))
            proj_y = int(proj_plane.shape[1]/2 + r*math.sin(phi)) if x-x_mid+pix_i >= 0 else int(proj_plane.shape[1]/2 - r*math.sin(phi))
            
            # Skip the pixel if it is outside the bounds of the output image
            if proj_x >= proj_plane.shape[0] or proj_y >= proj_plane.shape[1]:
                continue
            
            # Copy the pixel to the new location
            proj_plane[proj_x][proj_y] = img[pix_i][pix_j]
    
    # Determine the starting points for cropping
    start_x = 0 if x < 0 else x
    start_y = 0 if y < 0 else y
    
    # Return the warped image and the cropped image
    return proj_plane, proj_plane[start_x:start_x+224,start_y:start_y+224]
