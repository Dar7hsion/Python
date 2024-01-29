#Provided to you by Emerging Technology Institute
import cv2
import numpy as np
import mediapipe as mp # Google Library, it's open source

# Initialize the hand tracking module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the video capture
cap = cv2.VideoCapture(0)  # 0 for default camera

# Font settings for the text label
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 255, 0)
line_type = 2

#Thresholds
thumb_up_sensitivity = 1.98

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    ret2, debug = cap.read()

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with the hand tracking module
    results = hands.process(frame_rgb)

    # Check if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Iterate through each detected hand

            # Get the landmark positions
            landmark_list = []
            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                landmark_list.append((x, y))
                cv2.putText(debug, str(len(landmark_list) - 1), (x, y), font, font_scale, font_color, line_type)

            # Check if the peace sign gesture (V sign) is detected
            if len(landmark_list) >= 20:
                finger_tip_1 = landmark_list[8]  # Index finger tip landmark
                finger_tip_2 = landmark_list[12]  # Middle finger tip landmark
                palm_center = landmark_list[0]  # Palm center landmark
                finger_tip_3 = landmark_list[16] # Ring tip
                finger_tip_4 = landmark_list[20] # Pinky tip
                finger_tip_5 = landmark_list[4] # Thumb tip
                
                # Calculate the distance between the finger tips and the palm center
                dist_1 = cv2.norm(np.array(finger_tip_1) - np.array(palm_center))
                dist_2 = cv2.norm(np.array(finger_tip_2) - np.array(palm_center))
                dist_3 = cv2.norm(np.array(finger_tip_3) - np.array(palm_center))
                dist_4 = cv2.norm(np.array(finger_tip_4) - np.array(palm_center))
                dist_5 = cv2.norm(np.array(finger_tip_5) - np.array(palm_center))

                #print(dist_1, dist_2, dist_3, dist_4, dist_5)

                # Check if the distances are within a threshold to indicate a peace sign gesture
                if (dist_1 > max(dist_3, dist_4,dist_5)) and (dist_2 > max(dist_3, dist_4,dist_5)) and dist_3 < (dist_1-dist_3) and dist_4 < (dist_1-dist_4) and dist_5 < (dist_1-dist_5):
                    # Draw a text label for the peace sign gesture
                    cv2.putText(frame, 'Peace Sign', (finger_tip_1), font, font_scale, font_color, line_type)
                #Thumbs Up
                if dist_5 > max(dist_1,dist_2,dist_3,dist_4) and (dist_5/((dist_1+dist_2+dist_3+dist_4)/4)) > thumb_up_sensitivity:
                    # Draw a text label for the thumbs sign gesture
                    cv2.putText(frame, 'Thumbs Up', (finger_tip_5), font, font_scale, font_color, line_type)
                
                
                grip_distance = cv2.norm(np.array(finger_tip_5) - np.array(finger_tip_1))
                print(grip_distance)
                if grip_distance < 50:
                    
                    print("Grip",finger_tip_1)

            # Draw hand landmarks on the frame
            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * debug.shape[1])
                y = int(landmark.y * debug.shape[0])
                cv2.circle(debug, (x, y), 5, (0, 255, 0), -1)

    # Display the frame with hand landmarks
    cv2.imshow('Hand Tracking', frame)
    cv2.imshow('Debug Hand Tracking', debug)
    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()