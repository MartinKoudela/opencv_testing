import cv2

img = cv2.imread("./assets/example_img.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
