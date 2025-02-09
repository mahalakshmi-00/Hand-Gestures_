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

if len(landmark_list) >= 9:  # Ensure we have at least 9 landmarks (for fingers and palm)
    # Define indices of landmarks for fingertips and base of fingers
    base_of_thumb = 0  # Assuming thumb base landmark is at index 0
    tip_of_thumb = 4   # Assuming thumb tip landmark is at index 4
    base_of_index = 5   # Assuming index finger base landmark is at index 5
    tip_of_index = 8    # Assuming index finger tip landmark is at index 8

    # Check relative positions of landmarks to determine gesture
    if landmark_list[tip_of_thumb][1] < landmark_list[base_of_thumb][1] and \
       landmark_list[tip_of_index][1] < landmark_list[base_of_index][1]:
        gesture = "Palm"
    elif landmark_list[tip_of_thumb][1] > landmark_list[base_of_thumb][1] and \
         landmark_list[tip_of_index][1] < landmark_list[base_of_index][1]:
        gesture = "Fingers"

# Example of how to display gesture text on the frame
if gesture is not None:
    cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Display the frame with gesture text
cv2.imshow('Gesture Recognition', frame)
cv2.waitKey(1)

  
cap.release()
cv2.destroyAllWindows()
               
            

