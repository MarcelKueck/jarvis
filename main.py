import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr


api_key = "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"

lang = 'en'

openai.api_key = api_key

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                if "Jarvis" in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", message=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("text.mp3")
                    playsound.playsound("text.mp3")

            except Exception as e:
                print("Exception: " + str(e))

        return said
    
    get_audio()

