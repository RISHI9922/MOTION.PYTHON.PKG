import cv2


def detect_motion():
    
    cap = cv2.VideoCapture(0) 


    _, frame1 = cap.read()


    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    while True:

        _, frame2 = cap.read()


        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

       
        diff = cv2.absdiff(gray1, gray2)

    
        _, threshold = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)


        dilated = cv2.dilate(threshold, None, iterations=2)

       
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

       
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 500:
                continue
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Motion Detection", frame2)


        gray1 = gray2

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


detect_motion()
