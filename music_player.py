import pygame
import os

# Initialize PyGame mixer
pygame.mixer.init()

# Define music paths for each emotion
emotion_music = {
    "happy": "music/happy_song.mp3",
    "sad": "music/sad_song.mp3",
    "angry": "music/angry_song.mp3",
    "surprise": "music/surprise_song.mp3",
    "neutral": "music/neutral_song.mp3"
}

def play_music(emotion):
    """Play music based on the detected emotion."""
    if emotion in emotion_music:
        pygame.mixer.music.load(emotion_music[emotion])
        pygame.mixer.music.play()

    # Keep playing until the song ends
    while pygame.mixer.music.get_busy():
        continue
