import cv2

img = cv2.imread("C:\\Users\\hsoni\\Desktop\\goku.jpg")
resizedimg = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
print('img::',img.shape)
print('img::',resizedimg)
cv2.imshow("goku",img)
cv2.imshow("resized goku",resizedimg)
cv2.waitKey(2220)
cv2.destroyAllWindows()