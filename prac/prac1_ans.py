import cv2

# 讀取圖片
img = cv2.imread('../Domino.jpg')

# 轉換大小到 600x250
new_img = cv2.resize(img,(600,250)) 

# 顯示並儲存調整後的照片
cv2.imshow('domino',new_img)
cv2.imwrite('prac_new.jpg',new_img)

# 將調整後的照片轉為灰階
output = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

# 設定視窗名稱與大小
cv2.namedWindow('gray', cv2.WINDOW_NORMAL) 

# 顯示並儲存灰階照片
cv2.imshow('gray', output)
cv2.imwrite('prac_gray.jpg', output)

# 5秒後關閉視窗
cv2.waitKey(5000)
cv2.destroyAllWindows() 

