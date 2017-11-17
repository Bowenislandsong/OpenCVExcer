import cv2
import io

def showandwrite(filename, img):
	cv2.imshow(filename, img)
	cv2.imwrite(''.join([filename,".png"]),img)

src = cv2.imread("..//Test_images/Lenna.png",1)
showandwrite( "Original image", src)

graysrc = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
showandwrite("Input greyscale Image",graysrc)

threshold_type = 2; 
threshold_value = 128;


rat,dst = cv2.threshold (graysrc, threshold_value, 255, threshold_type)
showandwrite("Thresholded Image", dst )

current_threshold = 128;
max_threshold = 255;

th,binimg = cv2.threshold(graysrc, current_threshold, max_threshold, cv2.THRESH_BINARY);
showandwrite("Binary threshold",binimg)

threshold1 = 27
threshold2 = 125

tra,img_binary1 = cv2.threshold(graysrc,threshold1,max_threshold,cv2.THRESH_BINARY)
tra,binary_inv = cv2.threshold(graysrc,threshold2,max_threshold,cv2.THRESH_BINARY_INV)
img_thresholding = cv2.bitwise_and(img_binary1,binary_inv)
showandwrite("Band Thresholding",img_thresholding)


tra,semi_thresholded_image = cv2.threshold(graysrc,current_threshold,max_threshold,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
semi_thresholded_image = cv2.bitwise_and(graysrc,semi_thresholded_image)
showandwrite("Semi Thresholding",semi_thresholded_image)
    
img_adaptive_thresh = cv2.adaptiveThreshold(graysrc, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10)
showandwrite("Adaptive Thresholding",img_adaptive_thresh)
    
    




while (1):
	k = cv2.waitKey(33)
	if k==27:
		break