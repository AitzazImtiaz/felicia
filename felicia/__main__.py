import pyaudio
import speech_recognition as sr
import cleverbotfreeapi
import os

def main():
    recognizer = sr.Recognizer()
    
    while True:
        audio = None
        try:
            audio_input = input("Press Enter to start recording...")
            if audio_input == "":
                p = pyaudio.PyAudio()
                stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
                print("Recording... (Press Enter to stop)")
                
                frames = []
                while True:
                    try:
                        audio_chunk = stream.read(1024)
                        frames.append(audio_chunk)
                    except KeyboardInterrupt:
                        print("Stopped recording.")
                        break

                stream.stop_stream()
                stream.close()
                p.terminate()
                
                audio = b''.join(frames)
        except KeyboardInterrupt:
            break
        
        if audio:
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
