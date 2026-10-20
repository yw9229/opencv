import cv2

img = cv2.imread('../Domino.jpg')   # 讀取照片
img = cv2.resize(img,(650,650))     # 調整尺寸

#============================
#   濾波器
#============================

# # 高斯濾波器
# img1 = cv2.GaussianBlur(img,(5,5),0)    # 核心越大越模糊
# img2 = cv2.GaussianBlur(img,(15,15),0)

# # 中值濾波器
# img1 = cv2.medianBlur(img, 5)
# img2 = cv2.medianBlur(img, 15)

# # 雙邊濾波器
# img1 = cv2.bilateralFilter(img,50,10,1000)
# img2 = cv2.bilateralFilter(img,50,100,1000)

# # 顯示照片
# cv2.imshow('picture', img)
# cv2.imshow('filtered_picture1', img1)
# cv2.imshow('filtered_picture2', img2)

#============================
#   三種濾波器比較並儲存
#============================

# img1 = cv2.GaussianBlur(img,(15,15),0)
# img2 = cv2.medianBlur(img, 15)
# img3 = cv2.bilateralFilter(img,50,100,1000)

# cv2.imshow('picture', img)
# cv2.imshow('GaussianBlur_picture1', img1)
# cv2.imshow('MedianBlur_picture2', img2)
# cv2.imshow('BilateralFilter_picture3', img3)

# cv2.imwrite('GaussianBlur_Domino.jpg', img1)
# cv2.imwrite('MedianBlur_Domino.jpg', img2)
# cv2.imwrite('BilateralFilter_Domino.jpg', img3)


cv2.waitKey(0)
cv2.destroyAllWindows()