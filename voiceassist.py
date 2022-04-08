from dataclasses import dataclass
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import pyjokes


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not understanding message")
# sptext()            

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

# speechtx("helo and welcome to mumbai india")


if __name__ == '__main__':

    # if sptext().lower() =="hello world":
       data1=sptext().lower()

       if "your name" in data1:
           name = "my name is henry"
           speechtx(name)
       elif "old" in data1:
            age = "i am 22 years old"
            speechtx(age) 
       elif ' time' in data1:
           time = datetime.datetime.now().strftime("%I%M%p")
           speechtx(time)
       elif 'youtube' in data1:
           webbrowser.open("https://www.youtube.com/watch?v=OKuiyX5k6zg")

       elif "joke" in data1:
           joke_1 = pyjokes.get_joke(language="en" , category="neutral")
           print(joke_1)
           speechtx(joke_1)
