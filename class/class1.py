import cv2

#============================
#   顯示圖片
#============================
# # 讀取照片
# img = cv2.imread('../Domino.jpg')

# # 設定視窗名稱與大小
# cv2.namedWindow('picture', cv2.WINDOW_NORMAL)  # 設定視窗大小可調整

# # 顯示照片
# cv2.imshow('picture', img)

# # 數字為0:等待按下鍵盤任意鍵 單位:ms
# cv2.waitKey(0)

# # 關閉視窗
# cv2.destroyAllWindows()

#============================
#   顯示調整後的圖片並儲存
#============================

# img = cv2.imread('../Domino.jpg')

# # 影像尺寸調整
# img_resize = cv2.resize(img, (650, 650))

# # 儲存調整後的圖片
# cv2.imwrite('resized_Domino.jpg', img_resize)

# cv2.namedWindow('picture', cv2.WINDOW_NORMAL)  # 設定視窗大小可調整
# cv2.imshow('picture', img)
# cv2.imshow('resized_picture', img_resize)

# # 只有按下 p 才會關閉視窗
# while True:
#     key = cv2.waitKey(1) & 0xFF

#     if key == ord('p'):
#         break

# cv2.destroyAllWindows()

#============================
#   顯示調整後的圖片並儲存
#============================

# img = cv2.imread('../Domino.jpg')
# cv2.namedWindow('picture', cv2.WINDOW_NORMAL) 
# cv2.imshow('picture', img)

# # 將色彩圖片轉為灰階圖片
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# cv2.imwrite('togray_Domino.jpg', gray)  # 儲存灰階圖片
# cv2.namedWindow('gray_Domino', cv2.WINDOW_NORMAL)
# cv2.imshow('gray_Domino', gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()