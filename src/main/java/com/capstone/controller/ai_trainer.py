import numpy as np
import cv2
import time
import cvzone
from pose_module import PoseDetector

cap = cv2.VideoCapture(0)

ctime = 0
ptime = 0
direction = 0
push_ups = 0
ready = False  # New variable to check if the user is ready

b_color = (0, 0, 0)
blue_color = (190, 150, 37)

detector = PoseDetector()
while True:
    _, img = cap.read()
    img = detector.findPose(img)
    lmlist, bbox = detector.findPosition(img, draw=False)
    if lmlist:
        # Find angles for each arm
        a1, _ = detector.findAngle(lmlist[12][:2], lmlist[14][:2], lmlist[16][:2], img=img)
        a2, _ = detector.findAngle(lmlist[15][:2], lmlist[13][:2], lmlist[11][:2], img=img)

        # Check if the user is in the "ready" position
        if not ready:
            if 160 <= a1 <= 170 and 160 <= a2 <= 170:
                ready = True
                cvzone.putTextRect(img, "Ready! Start Push-ups", (200, 50), 2, 2, colorT=(0, 255, 0), colorR=(255, 255, 255), colorB=b_color, border=1)
            else:
                cvzone.putTextRect(img, "Get into position", (200, 50), 2, 2, colorT=(0, 0, 255), colorR=(255, 255, 255), colorB=b_color, border=1)
        else:
            # Calculate the percentage and bar values only if ready
            per_val1 = int(np.interp(a1, (90, 170), (100, 0)))
            per_val2 = int(np.interp(a2, (90, 170), (100, 0)))
            bar_val1 = int(np.interp(per_val1, (0, 100), (40+350, 40)))
            bar_val2 = int(np.interp(per_val2, (0, 100), (40+350, 40)))

            # Draw bars
            cv2.rectangle(img, (570, bar_val1), (570 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
            cv2.rectangle(img, (570, 40), (570 + 35, 40 + 350), (), 2)
            cv2.rectangle(img, (35, bar_val2), (35 + 35, 40 + 350), (0, 0, 255), cv2.FILLED)
            cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (), 2)

            # Display percentages
            cvzone.putTextRect(img, f"{per_val1} %", (570, 25), 1.3, 2, colorT=blue_color, colorR=(255, 255, 255), border=1, colorB=b_color)
            cvzone.putTextRect(img, f"{per_val2} %", (25, 25), 1.3, 2, colorT=blue_color, colorR=(255, 255, 255), border=1, colorB=b_color)

            # Push-up counting logic
            if per_val1 == 100 and per_val2 == 100:
                if direction == 0:
                    push_ups += 0.5
                    direction = 1
                    color = (0, 255, 0)
            elif per_val1 == 0 and per_val2 == 0:
                if direction == 1:
                    push_ups += 0.5
                    direction = 0
                    color = (0, 255, 0)
            else:
                color = (0, 0, 255)

            # Display push-up count
            cvzone.putTextRect(img, f"Push-ups : {int(push_ups)}", (200, 35), 2, 2, colorT=(0, 0, 255), colorR=(0, 255, 0), colorB=(), border=1)
            cvzone.putTextRect(img, "Left Hand", (15, 350+100), 1.5, 2, colorT=(255, 255, 255), colorR=blue_color, colorB=b_color, border=1)
            cvzone.putTextRect(img, "Right Hand", (485, 350+100), 1.5, 2, colorT=(255, 255, 255), colorR=blue_color, colorB=b_color, border=1)

            print(push_ups)

    # FPS calculation
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.imshow("Push-ups Counter", img)
    if cv2.waitKey(1) == ord("q"):
        break
