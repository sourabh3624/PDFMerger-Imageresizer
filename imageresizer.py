import cv2
source="jawa perak.jpg"
destination='newImage.jpg'
scale_percent=50
src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
cv2.imshow("title",src)
scale_percent=50
new_width=int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)

output=cv2.resize(src,(new_width,new_height))
cv2.imwrite(destination,output)
cv2.waitKey(0)