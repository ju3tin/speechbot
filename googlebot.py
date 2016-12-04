import speech_recognition as sr

import os
dir = os.path.dirname(__file__)
folder = os.path.join(dir) 

import sys
sys.path.append(folder)

import QA.dataInterface as dataInt 
import textToSpeech

def googleSpeechToTextWithWatsonSpeechToTest():
    r = sr.Recognizer()
    with sr.WavFile("test.wav") as source: # use "test.wav" as the audio source
      r.energy_threshold = 4000
      audio = r.record(source) # extract audio data from the file
      try:
        sentence =   r.recognize_google(audio)
        print("You said " + sentence)  # recognize speech using Google Speech Recognition
        dataInt.gatherData()
        bestAnswer = dataInt.returnBestAnswer( sentence  )
        print (bestAnswer)
        textToSpeech.textToSpeech(bestAnswer)
      except IndexError: # the API key didn't work
        print("No internet connection")
      except KeyError: # the API key didn't work
        print("Invalid API key or quota maxed out")
      except LookupError: # speech is unintelligible
        print("Could not understand audio")

if __name__ == "__main__":
    googleSpeechToTextWithWatsonSpeechToTest()
