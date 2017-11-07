import cv2
import io

# this was fun -- Bowen


src = cv2.imread("Test_images/Lenna.png", 1)
cv2.namedWindow( 'Original image', cv2.WINDOW_AUTOSIZE );
cv2.imshow( "Original image", src);


R,G,B = cv2.split(src);
cv2.imshow("Red",R);
cv2.imshow("Green",G);
cv2.imshow("Blue",B);

ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCR_CB);
y,cb,cr = cv2.split(ycrcb_image)
cv2.imshow("Y",y);
cv2.imshow("Cb",cb);
cv2.imshow("Cr",cr);

HSV_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV);
h,s,v = cv2.split(HSV_image)
cv2.imshow("Hue",  h);
cv2.imshow("Saturation", s);
cv2.imshow("Value", v);

while (1):
	k = cv2.waitKey(33)
	if k==27:
		break
