import cv2
import numpy as np

# ============================
#   找出圖片中的所有輪廓
# ============================

# # 建立圖片
# img = np.zeros((400, 500), dtype=np.uint8)  # 建立黑色圖片

# cv2.rectangle(img, (50, 50), (180, 180), 255, -1)   # 第一個白色矩形
# cv2.rectangle(img, (80, 80), (150, 150), 0, -1)     # 在第一個矩形中間挖出黑色區域
# cv2.circle(img, (320, 120), 65, 255, -1)       # 白色圓形
# cv2.rectangle(img, (180, 270), (350, 350), 255, -1)     # 第二個白色矩形


# # 尋找輪廓
# # 實驗 cv2.RETR_EXTERNAL 和 cv2.RETR_TREE 差別
# contours, hierarchy = cv2.findContours(
#     img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE     
# )

# # 轉換成彩色圖片，方便畫出綠色輪廓
# result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# # 繪製所有輪廓
# cv2.drawContours(result, contours, -1, (0, 255, 0), 3)

# # 印出輪廓數量
# print('輪廓數量：', len(contours))

# cv2.imshow('Original', img)
# cv2.imshow('Contours', result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ============================
#   描繪圖片的輪廓
# ============================

# # 讀取圖片
# img = cv2.imread('../Domino.jpg')
# img = cv2.resize(img, (650, 650))


# # 轉換灰階
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 二值化
# ret, binary = cv2.threshold(
#     gray, 128, 255, cv2.THRESH_BINARY
# )

# # 尋找輪廓
# contours, hierarchy = cv2.findContours(
#     img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
# )

# # 複製原始圖片
# result = img.copy()

# # 繪製輪廓
# cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

# print('輪廓數量：', len(contours))

# # 顯示圖片
# cv2.imshow('Original', img)
# cv2.imshow('Binary', binary)
# cv2.imshow('Contours', result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

