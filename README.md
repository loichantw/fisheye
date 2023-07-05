# Useful Tool
## Spherical Projection Image Warping
This repository contains a Python implementation of a spherical projection image warping algorithm, which is a useful tool for warping fisheye images. The code takes an input image and parameters for offsets and a focal length, and applies a spherical projection to warp the image.

## Usage
The main function is warp(img, x=0, y=0, f=100), where:

img is the input image (a numpy array).
x and y are offsets applied to the image (default is 0).
f is the focal length that controls the intensity of the warping effect (default is 100).
The function returns the warped image and a version cropped to the original image size.
## Example
``` python
import cv2
img = cv2.imread('input.jpg')
warped_img, cropped_img = warp(img, x=10, y=10, f=100)
cv2.imwrite('warped.jpg', warped_img)
cv2.imwrite('cropped.jpg', cropped_img)
``` 
## Citation
If you use this code in your research, please cite the following papers:

- Y.-H. Li, I-C. Lo, and H. H. Chen, “Deep face rectification for 360 dual-fisheye cameras,” IEEE Trans. Image Process., vol. 30, DOI 10.1109/TIP.2020.3019661, pp. 264-276, 2021
- I-C. Lo, K.-T. Shih, and H. H. Chen, “Efficient and accurate stitching for 360° dual-fisheye images and videos,” IEEE Trans. Image Process., vol. 31, pp. 251-262, DOI: 10.1109/TIP.20, Jan. 2022
- Y.-C. Lo, C.-C. Huang, Y.-F. Tsai, I-C. Lo, A.-Y. Wu, and H. H. Chen, “Face recognition for fisheye images,” in Proc. IEEE Int. Conf. Image Process., pp. 146-150, Oct. 2022

## License
This project is licensed under the terms of the MIT license.


