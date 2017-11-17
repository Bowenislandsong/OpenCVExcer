import cv2
import io
import numpy as np

def add_sault_peper_Noise(mat, pa, pb):
    rows,cols,ch = mat.shape
    amount1 = int(rows*cols*pa)
    amount2 = int(rows*cols*pb)
    for i in range(amount1):
        mat[np.random.randint(0,rows-1), np.random.randint(0,cols-1)]=0
    for i in range(amount2):
        mat[np.random.randint(0,rows-1), np.random.randint(0,cols-1)]=255

def add_gaussian_Noise(mat, mean, sig):
	mattemp = mat.copy()
	cv2.randn(mattemp, mean, sig)
	cv2.add(mat, mattemp, mat)


def showandwrite(filename, img):
	cv2.imshow(filename, img)
	cv2.imwrite(''.join([filename,".png"]),img)


src = cv2.imread("../Test_images/Lenna.png", 1)
showandwrite( "Original image", src)

noise_img = src.copy(); 
mean = 0;			
sigma = 50;		
win = (7,7);
add_gaussian_Noise(noise_img, mean, sigma);
showandwrite( "Gaussian Noise", noise_img);


noise_dst = noise_img.copy();
cv2.boxFilter(noise_dst,-1, win)
showandwrite( "GN Box filter", noise_dst);

noise_dst1 = noise_img.copy();
cv2.GaussianBlur(noise_dst1, win, 1.5)
showandwrite( "GN Gaussian filter", noise_dst1);

noise_dst2 = noise_img.copy();
cv2.medianBlur(noise_dst2, 5)
showandwrite( "GN Median filter", noise_dst1);

noise_img2 = src.copy();
pa = 0.01
pb = 0.01
add_sault_peper_Noise(noise_img2,pa,pb)
showandwrite("Salt and Pepper Noise", noise_img2)

noise_dst3 = noise_img2.copy();
cv2.boxFilter(noise_img2,-1, win)
showandwrite( "SP Box filter", noise_dst3);

noise_dst4 = noise_img.copy();
cv2.GaussianBlur(noise_dst4, win, 1.5)
showandwrite( "SP Gaussian filter", noise_dst4);

noise_dst5 = noise_img.copy();
cv2.medianBlur(noise_dst5, 5)
showandwrite( "SP Median filter", noise_dst5);


while (1):
	k = cv2.waitKey(33)
	if k==27:
		break