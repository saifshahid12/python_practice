import speech_recognition as sr
import pyttsx3

# pip install pocketsphinx 

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak (text):
    engine.say (text)
    engine.runAndWait()

def processcommand(c):
    print(c)
    

if __name__=="__main__":
    speak("initiallizing jarvis....")
    while True:
    # listen for tha wake word jarvis:
    # obtain audio from the microphone 

        r=sr.Recognizer()
        # with sr.Microphone() as source:
        #      print("listening..")
        #      audio =r.listen(source, timeout=2, phrase_time_limit=1)

        print("recognizing...")
# recognize speech using sphinx
        try:
            with sr.Microphone() as source:
               print("listening..")
               audio =r.listen(source, timeout=2, phrase_time_limit=1)

            word=r.recognize_google(audio)
            print(command)                          

            if(word.lower()=="jarvis"):
                speak("ya")

             # list for command :
                with sr.Microphone() as source:
                    print("jarvis active..")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)
        except Exception as e:
            print("error; {0}".format(e))
        