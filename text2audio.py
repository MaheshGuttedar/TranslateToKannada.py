from gtts import gTTS
from googletrans import Translator
import os
import pygame

from googletrans import Translator

def translate_english_to_kannada(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='kn')
    return translated_text.text

# Example usage:
english_text = "Once upon a time in a small, picturesque village, there lived a curious young girl named Lily. She had a deep fascination for the stars and spent her nights stargazing from her bedroom window. One clear night, she noticed a shooting star streak across the sky and made a heartfelt wish."

kannada_translation = translate_english_to_kannada(english_text)
print(f"English: {english_text}")
print(f"Kannada: {kannada_translation}")

# Input your text here or load it from a file
kannada_text = kannada_translation

# Optional: Translate text to Kannada
translator = Translator()
kannada_text = translator.translate(kannada_text, src='en', dest='kn').text

# Convert text to speech in Kannada
tts = gTTS(text=kannada_text, lang='kn')

# Save the audio as an MP3 file
tts.save('output_audio.mp3')

# Initialize pygame mixer
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load('output_audio.mp3')

# Play the audio
pygame.mixer.music.play()

# Wait for the audio to finish playing
while pygame.mixer.music.get_busy():
    continue

# Clean up: Delete the audio file (optional)
os.remove('output_audio.mp3')
