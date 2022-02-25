import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    print(frame.shape)
    cv.imshow("Live Video", frame)
    grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("GRAY", grayscale)


    if cv.waitKey(100) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
