import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install specchRecognition
import wikipedia
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''it will speak the thing that has given in argument'''
    engine.say(audio)
    engine.runAndWait()
def wishme():
    '''this will greet you whenever you call this function'''
    hour=datetime.datetime.now().hour
    if(hour>=0 and hour<12):
        speak("good morning ")
    elif(hour>=12 and hour<16):
        speak("good afternoon ")
    else:
        speak("good evening ")
    speak("hello i am ross . how can i help you")
def takecommand():
    '''this will recognise your voice '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
if __name__ == '__main__':
    wishme()
    start='start'
    while True:
         query=takecommand().lower()

         #logic based in query
         if 'wikipedia' in query:
             speak("searching  wikipedia...")
             query=query.replace("wikipedia","")
             result=wikipedia.summary(query,sentences=2)
             speak("according to wikipedia")
             speak(result)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")

         elif 'open google' in query:
             webbrowser.open("google.com")

         elif 'play music' in query:
             webbrowser.open("gaana.com")

         elif 'time' in query:
             str=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir the time is {str}")

         elif 'about you' in query:
                speak("my name is ross, i am created by kunal ")


