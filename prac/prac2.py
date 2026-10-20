import cv2

# 讀取灰階圖片並改變尺寸
img = cv2.imread('../Domino.jpg', 0)
img = cv2.resize(img, (650, 650))

# 複製圖片
img2 = img.copy()

# 取得圖片高度與寬度
height, width = img.shape

# 設定閾值
threshold = 128

# 使用雙層 for 迴圈進行二值化
for y in range(__________):
    for x in range(__________):

        # 讀取像素值
        pixel = img[__________]

        # 判斷像素值
        if pixel >= __________:
            img2[__________] = __________
        else:
            img2[__________] = __________

# 顯示圖片
cv2.imshow('Original', img)
cv2.imshow('Binary', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()