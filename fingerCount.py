import mediapipe as mp
import cv2
#PRESS 'Q' TO CLOSE WINDOW

video =  cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

while True:
    _, img = video.read()
    img =cv2.flip(img,1)
    imgRGB =  cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h,w,_ = img.shape
    pontos = []
    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
            for id,cord in enumerate(points.landmark):
                cx,cy = int(cord.x*w), int(cord.y*h)
                cv2.putText(img,str(id),(cx,cy+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                pontos.append((cx,cy))

        dedos = [8,12,16,20]
        contador = 0
        if points:
            if pontos[4][0] < pontos[2][0]:
                contador +=1
            for x in dedos:
                if pontos[x][1] < pontos [x-2][1]:
                    contador += 1

        cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)

    cv2.imshow("Colmeia", img)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cv2.destroyAllWindows()