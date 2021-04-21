import speech_recognition as sr
import webbrowser
from textblob import  TextBlob
import time
import playsound
import os
import random
from gtts import gTTS
from time import  ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            chat_speak(ask)
        audio = r.listen(source)
        text = ''

        try:
            text = r.recognize_google(audio)
            print('You said: {}'.format(text))
            tb = TextBlob (text)
            print(text)
            print(tb.sentiment)
        except sr.UnknownValueError:
            chat_speak('Sorry, I did not get that')
        return text

def chat_speak(audio_string):
    tts = gTTS(text = audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(text):
    if 'hello' in text:
        chat_speak('Hi')
    if 'what is your name' in text:
        chat_speak('My name is FriendChat,what is your name?')
    if 'how is it going' in text:
        chat_speak('Good,how are you doing')
    if 'what are you doing' in text:
        chat_speak('I am talking to you, what are you doing')
    if 'my name is' in text:
        chat_speak('nice to meet you')
    if 'thanks' in text:
        chat_speak('My pleasure')
    if 'no problem' in text:
        chat_speak('You are sweet')
    if 'what time is it' in text:
        chat_speak(ctime())
    if 'good' in text:
        chat_speak('I am glad for you')
    if 'search' in text:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        chat_speak('Here is what I found for' + search)
    if 'find location' in text:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        chat_speak('Here is the location of' + location)
    if 'exit' in text:
        exit()

time.sleep(1)
chat_speak('How can I help you?')
while 1:
    text = record_audio()
    respond(text)