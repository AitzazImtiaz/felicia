import speech_recognition as sr
import cleverbotfreeapi
import os

def main():
    recognizer = sr.Recognizer()
    
    while True:
        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source)
        
        try:
            inp = recognizer.recognize_google(audio)
            print("You >> " + inp)
            
            out = cleverbotfreeapi.cleverbot(inp, session="Deftera")
            print("Felicia >> " + out)
            
            os.system(f"termux-tts-speak '{out}'")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()
