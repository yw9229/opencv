import cv2


# 讀取圖片
img = __________

# 轉換大小到 600x250
new_img = cv2.resize(img,__________) 

# 顯示並儲存調整後的照片
__________
__________

# 將調整後的照片轉為灰階
output = cv2.cvtColor(new_img, __________)

# 設定視窗名稱與大小
cv2.namedWindow('gray', cv2.WINDOW_NORMAL) 

# 顯示並儲存灰階照片
__________
__________

# 5秒後關閉視窗
cv2.waitKey(__________)
cv2.destroyAllWindows() 

