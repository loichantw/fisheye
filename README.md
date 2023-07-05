# fisheye-warping
Spherical Projection Image Warping

The provided code implements a spherical projection image warping algorithm. It takes an input image and parameters for offsets (x, y) and a focal length (f). Each pixel in the input image is projected onto a sphere, with the pixel's distance from the image center determining the angle of projection (theta), and the direction from the center determining the azimuthal angle (phi). The pixel is then mapped to a new location in the output image based on these angles and the focal length, creating a warped effect. The algorithm returns the warped image and a version cropped to the original image size.
