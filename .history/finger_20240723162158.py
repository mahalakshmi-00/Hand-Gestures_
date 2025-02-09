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

    # Convert the frame from BGR to RGB color format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(frame_rgb)

    # Draw landmarks and recognize gestures if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks and connections on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Calculate landmark positions and store in landmark_list
            landmark_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([cx, cy])

            # Gesture recognition logic
            gesture = None

            # Check for Thumbs Up gesture
            if len(landmark_list) >= 21:  # Assuming at least 21 landmarks for thumbs up
                if (landmark_list[4][1] < landmark_list[3][1] and
                    landmark_list[8][1] < landmark_list[7][1] and
                    landmark_list[12][1] < landmark_list[11][1] and
                    landmark_list[16][1] < landmark_list[15][1]):
                    gesture = "Thumbs Up"

            # Check for Peace Sign gesture
            if len(landmark_list) >= 19:  # Assuming at least 19 landmarks for peace sign
                if (landmark_list[8][1] < landmark_list[6][1] and
                    landmark_list[12][1] < landmark_list[10][1]):
                    gesture = "Peace Sign"

            # Check for Fist gesture
            if len(landmark_list) >= 9:  # Assuming at least 9 landmarks for fist
                if (landmark_list[4][1] > landmark_list[3][1] and
                    landmark_list[8][1] > landmark_list[7][1]):
                    gesture = "Fist"

            # Check for Palm gesture
            if len(landmark_list) >= 9:  # Assuming at least 9 landmarks for palm
                if (landmark_list[4][1] < landmark_list[3][1] and
                    landmark_list[8][1] < landmark_list[6][1]):
                    gesture = "Palm"

            # Check for Fingers gesture
            if len(landmark_list) >= 9:  # Assuming at least 9 landmarks for fingers
                if (landmark_list[4][1] > landmark_list[3][1] and
                    landmark_list[8][1] < landmark_list[6][1]):
                    gesture = "Fingers"

            # Example of how to display gesture text on the frame
            if gesture is not None:
                cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the annotated frame with gesture text
    cv2.imshow('Hand Gesture Recognition', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
