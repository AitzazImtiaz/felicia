import cleverbotfreeapi
import os
import subprocess

def main():
    while True:
        try:
            inp = subprocess.getoutput("termux-speech-to-text")
            if not inp:
                print("No input detected. Try again.")
                continue
            
            print("You >> " + inp)
            out = cleverbotfreeapi.cleverbot(inp, session="Deftera")
            print("Felicia >> " + out)

            # Use Termux's TTS to speak the response
            os.system(f"termux-tts-speak '{out}'")
        except Exception as e:
            print("An error occurred:", str(e))
            continue

if __name__ == "__main__":
    main()
