# AI-Powered-Real-Time-Emotion-Based-Music-Player
AI-Powered Real-Time Emotion-Based Music Player is an intelligent music player that uses AI to detect emotions through your webcam in real-time. Based on your facial expressions, it plays music that matches your mood. The project is built using Python, OpenCV for emotion detection, and PyGame for playing music.
# AI-Powered Real-Time Emotion-Based Music Player

## Overview
This project is an AI-powered music player that detects real-time emotions using your webcam and plays music accordingly. The system leverages a pre-trained facial expression recognition model to determine emotions such as happiness, sadness, anger, and more, and then plays a suitable track based on the detected emotion.

## Features
- Real-time emotion detection using OpenCV and the `fer` (Facial Expression Recognition) package.
- Plays different music tracks based on detected emotions such as:
  - Happy
  - Sad
  - Angry
  - Surprise
  - Neutral
- Music playback functionality powered by PyGame.


## Setup Instructions

### Prerequisites
- Python 3.x
- A webcam

### Required Libraries
To install the required Python libraries, run the following command:

```bash
pip install opencv-python tensorflow keras pygame numpy fer
emotion_music_player/
├── emotions.py
├── music_player.py
├── music/
│   ├── happy_song.mp3
│   ├── sad_song.mp3
│   ├── angry_song.mp3
│   ├── surprise_song.mp3
│   └── neutral_song.mp3


Running the Project
Place MP3 files in the music/ folder corresponding to each emotion:

happy_song.mp3
sad_song.mp3
angry_song.mp3
surprise_song.mp3
neutral_song.mp3
Run the following command to start the emotion detection and music player:

bash
Copy code
python emotions.py
The webcam will capture your facial expressions in real time, detect the dominant emotion, and play the corresponding song.
Customization
You can easily add or replace songs for each emotion by placing new MP3 files in the music/ folder and updating their names in music_player.py.

Future Improvements
Integration with Spotify or other streaming services.
Enhancing the emotion detection model for higher accuracy.
Adding support for more emotions and mood categories.

