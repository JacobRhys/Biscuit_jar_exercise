import serial
import cv2
import mediapipe as mp
import numpy as np
import time


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Open the serial port (change the port number to the port of your Arduino)
port = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

cap = cv2.VideoCapture(0)

starjumps, goal, pose = 0, 5, False

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
        
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = pose.process(frame_rgb)
        
        if results.pose_landmarks:
            left_hand_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            right_hand_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
            left_shoulder_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            right_shoulder_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            left_hip_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            right_hip_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
            

            if (left_hand_landmark.y < left_hip_landmark.y and right_hand_landmark.y < right_hip_landmark.y):
                newPose = False
            elif (left_hand_landmark.y > left_shoulder_landmark.y and right_hand_landmark.y > right_shoulder_landmark.y):
                newPose = True
            
            if (newPose != pose):
                if (newPose):
                    starjumps += 1
                pose = newPose
        
        annotated_frame = frame.copy()

        if goal <= starjumps:
            command = "open"
            time.sleep(15)
            command = "close"
            starjumps = 0

                
        mp_drawing.draw_landmarks(
            annotated_frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        cv2.imshow('Mediapipe Feed', annotated_frame)

        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    print (command)
    if command == "open":
        port.write(bytes("open", 'utf-8'))
    elif command == "close":
        port.write(bytes("close", 'utf-8'))
