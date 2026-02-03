import cv2

# read the iamge
img = cv2.imread("Ironman.jpg")

# check if the image was laoded successfully
if img is None:
    print("Image not found: put Ironman.jpg in the same folder or use a full path")
    raise SystemExit(1)

# resize, convert and detect edges
img = cv2.resize(img, (500, 400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

#display the images
cv2.imshow("Ironman", img)
cv2.imshow("Gray Ironman", gray)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
