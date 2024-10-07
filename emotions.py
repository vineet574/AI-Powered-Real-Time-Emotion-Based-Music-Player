import cv2
from fer import FER
from music_player import play_music

# Load the emotion detector
emotion_detector = FER()

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Analyze the frame to detect emotions
    emotions = emotion_detector.detect_emotions(frame)
    
    # If emotions are detected, play corresponding music
    if emotions:
        emotion = emotions[0]["emotions"]
        dominant_emotion = max(emotion, key=emotion.get)
        print("Detected Emotion: ", dominant_emotion)
        play_music(dominant_emotion)
        cv2.putText(frame, f"{dominant_emotion}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Emotion Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
