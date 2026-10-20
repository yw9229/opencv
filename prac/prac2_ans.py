import cv2

img = cv2.imread('../Domino.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (650, 650))
img2 = img.copy()

height, width = img.shape
threshold = 128

for y in range(height):
    for x in range(width):

        pixel = img[y, x]

        if pixel >= threshold:
            img2[y, x] = 255
        else:
            img2[y, x] = 0

cv2.imshow('Original', img)
cv2.imshow('Binary', img2)
cv2.imwrite('Binary.jpg', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()