import cv2
import io

# this was fun -- Bowen

x = 20
y = 25

def showandwrite(filename, img):
	cv2.imshow(filename, img)
	cv2.imwrite(''.join([filename,".png"]),img)



src = cv2.imread("../Test_images/Lenna.png", 1)
print("For RGB ",str(src[x,y]))
#cv2.namedWindow( 'Original image', cv2.WINDOW_AUTOSIZE );
#cv2.imshow( "Original image", src);
showandwrite( "Original image", src)

ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCR_CB);
print("For YCbCr ",str(ycrcb_image[x,y]))

HSV_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV);
print("For HSV ",str(HSV_image[x,y]))

R,G,B = cv2.split(src);
showandwrite("Red",R);
showandwrite("Green",G);
showandwrite("Blue",B);


y,cb,cr = cv2.split(ycrcb_image)
showandwrite("Y",y);
showandwrite("Cb",cb);
showandwrite("Cr",cr);


h,s,v = cv2.split(HSV_image)
showandwrite("Hue",  h);
showandwrite("Saturation", s);
showandwrite("Value", v);

#print("The RGB values are: Blue " + src[x,y,0] +" Green "+ src[x,y,1] +" red "+ src[x,y,2] )

while (1):
	k = cv2.waitKey(33)
	if k==27:
		break




