# OpenCVExcer

## Exercise 1

A program reads the cvMat object from rows to column to type. We can specify the type of pixels, typically by specifying channels. The order of the pixel structure is bit depth (number of values can be held), models of color spaces, and number of channels. 

## Exercise 2

1. The outputs are the intensity of the specified value. For example blue has the intensity of the blue in each pixel and displayed as gray scale. Since there is only one element of the RGB is distracted, the intensity value can only differentiate from white and black. White being high value. 

2. For the Lena image, the values at [20 25]:
('For RGB ', '[106 122 225]')
('For YCbCr ', '[151 181 103]')
('For HSV ', '[  4 135 225]')

I also found the splits, while not assigned to the photo, is still assigning values.

## Exercise 3

As we increase the Interpolation filter window, the image becomes more blurry. 

Intuitively, Gaussian filter works better for Gaussian noise. The Median filter works better for salt and pepper noise. since saltNpepper noise are extreme values that are not going to be median value. it will always be ruled out by the filter. 

## Exercise 4

1. Different Threshold values result in different effects. The "Bitterness" is based on different input and the expected result.

2. Binary thresholding is only showing 2 colors and will not show details of the picture. The filter is solely based on intensity of the pixel value.

3. The adaptive filter shows more tolerance in deciding threshold values. The designed of such threshold value has more tolerance on the input.