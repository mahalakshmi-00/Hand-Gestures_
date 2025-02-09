import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmark_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([cx, cy])
            gesture = None

            #Thumbs Up gesture
            if len(landmark_list) >= 21: 
                if (landmark_list[4][1] < landmark_list[3][1] and
                    landmark_list[8][1] < landmark_list[7][1] and
                    landmark_list[12][1] < landmark_list[11][1] and
                    landmark_list[16][1] < landmark_list[15][1]):
                    gesture = "Thumbs Up"
            #Fist gesture
            if len(landmark_list) >= 9:  
                if (landmark_list[4][1] > landmark_list[3][1] and
                    landmark_list[8][1] > landmark_list[7][1]):
                    gesture = "Fist"
            #Palm gesture
            if len(landmark_list) >= 9:  
                if (landmark_list[4][1] < landmark_list[3][1] and
                    landmark_list[8][1] < landmark_list[6][1]):
                    gesture = "Palm"
            #Up gesture
            if len(landmark_list) >= 9:  
                if (landmark_list[4][1] > landmark_list[3][1] and
                    landmark_list[8][1] < landmark_list[6][1]):
                    gesture = "Fingers"
            if gesture is not None:
                cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
