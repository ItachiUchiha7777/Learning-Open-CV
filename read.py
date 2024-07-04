import cv2 as cv
img=cv.imread("photos\Cute dog - funny animals- shiba dog.jpeg")
cv.imshow("cat",img)
cv.waitKey(0)


def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[0]*scale)
    height=int(frame.shape[1]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture("videos\Jordan Peterson_ Fix Yourself Before It's Too Late.mp4")
while True:
    isTrue,frame=capture.read()
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
     break
capture.release()
cv.destroyAllWindows()