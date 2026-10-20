import cv2

img = cv2.imread('../Domino.jpg')   # 讀取照片
img = cv2.resize(img,(650,650))     # 調整尺寸

#============================
#   讀取像素數值
#============================

# # 取得圖片資訊
# print('圖片形狀：', img.shape)
# print('圖片高度：', img.shape[0])
# print('圖片寬度：', img.shape[1])
# print('圖片通道數：', img.shape[2])

# # 讀取指定位置的像素
# print('座標(0,0)的像素：', img[0, 0]) # B, G, R
# print('座標(50,100)的像素：', img[50, 100])

#============================
#   修改單一像素或局部區域
#============================

# # 修改指定像素設為紅色
# img[50, 100] = [0, 0, 255]

# # 分別修改 B、G、R
# img[60, 100, 0] = 255
# img[60, 100, 1] = 0
# img[60, 100, 2] = 0

# # 將指定的 100×100 像素區域設為綠色
# # 第 100～199 列（Y 軸，垂直方向）
# # 第 100～199 欄（X 軸，水平方向）
# img[100:200, 100:200] = [0, 255, 0] 

# cv2.imshow('Result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#==================================
#   使用陣列切片修改整張圖片的通道
#==================================

# # 複製圖片，避免修改原圖
# img1 = img.copy()
# img2 = img.copy()
# img3 = img.copy()

# # 修改整張圖片的 B 通道
# img1[:, :, 0] = 70

# # 修改整張圖片的 G 通道
# img2[:, :, 1] = 70

# # 修改整張圖片的 R 通道
# img3[:, :, 2] = 70

# # 顯示圖片
# cv2.imshow('Original', img)
# cv2.imshow('Blue = 70', img1)
# cv2.imshow('Green = 70', img2)
# cv2.imshow('Red = 70', img3)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#==================================
#   使用 for 迴圈修改整張圖片的通道
#==================================

# img1 = img.copy()

# # 取得圖片高度及寬度
# height, width = img1.shape[:2]

# # 使用雙層迴圈修改整張圖片
# for y in range(height):
#     for x in range(width):
#         img1[y, x, 0] = 70

# cv2.imshow('Original', img)
# cv2.imshow('Result', img1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#==================================
#   二值化函式介紹  
#==================================

# # 將圖片轉成灰階
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 二值化
# ret, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# # 顯示圖片
# cv2.imshow('Original', img)
# cv2.imshow('Binary', binary)

# cv2.waitKey(0)
# cv2.destroyAllWindows()