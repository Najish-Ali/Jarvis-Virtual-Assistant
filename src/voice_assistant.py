import os
import pygame
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
from command_processor import process_command
from ai_processor import ai_process
from datetime import time

# Class Definition: VoiceAssistant
class VoiceAssistant:
  # __init__: Constructor method that initializes
  def __init__(self):
    # An instance of Recognizer from the speech_recognition library.
    self.recognizer = sr.Recognizer()
    # An instance of pyttsx3's text-to-speech engine (though it’s not used in this script).
    self.engine = pyttsx3.init()
    # Initializes the mixer module of pygame for playing sounds.
    pygame.mixer.init()
    # The keyword that activates the assistant (set to "jarvis").
    self.wake_word = "jarvis"

  # method
  def speak(self, text):
    # Converts the text into speech and saves it as temp.mp3.
    tts = gTTS(text=text, lang='en')  # Removed the invalid 'tid' argument
    tts.save("temp.mp3")
    # Loads and plays temp.mp3 using pygame
    pygame.mixer_music.load("temp.mp3")
    pygame.mixer_music.play()
    # Waits until the audio is done playing with while condition.
    while pygame.mixer_music.get_busy():
      pygame.time.Clock().tick(10)
    # Cleans up by unloading the audio and deleting temp.mp3
    pygame.mixer_music.unload()
    os.remove("temp.mp3")

  # method
  def run(self):
    self.speak("Initializing Jarvis....")
    while True:
      # Listens for audio input through the microphone.
      with sr.Microphone() as source:
        print("Listening.......")
        # Records audio with a timeout of 2 seconds and a maximum phrase length of 3 seconds.
        audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=3)
      try:
        # Converts the recorded audio into text using Google's speech recognition API.
        text = self.recognizer.recognize_google(audio)
        # If the recognized text matches the wake word ("jarvis")
        if text.lower() == self.wake_word:
          # Announces activation.
          self.speak("Hello, How May i help you Sir...")
          # Listens for the next command.
          with sr.Microphone() as source:
            print("Jarvis Activate.....")
            # Processes the command with process_command, 
            # passing the command, the speak method for responses, 
            # and ai_process
            audio = self.recognizer.listen(source)
            command = self.recognizer.recognize_google(audio)
            process_command(command, self.speak, ai_process)
        else:
          print("Wake Word Not Recognized..")
      except Exception as e:
        print(f"An unexpected error occurred {e}")
      # Waits for 1 second before listening again.
      time.sleep(1)