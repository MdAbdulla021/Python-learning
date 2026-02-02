import cv2 as cv
img = cv.imread("Ironman.jpg")
cv.imshow("Ironman",img)
cv.waitKey(0)
cv.destroyAllWindows()
if img is None:
    print("Image not found")
