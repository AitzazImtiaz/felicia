import cleverbotfreeapi
import os
import subprocess

def main():
    first_inp = "Hi"  # Initial input
    session = "Deftera"
    
    while True:
        print("You >> " + first_inp)
        out = cleverbotfreeapi.cleverbot(first_inp, session=session)
        print("AI 1 >> " + out)
        
        if out.strip():  # Check if Cleverbot provided a non-empty response
            second_inp = out
            print("AI 2 >> " + second_inp)
            fout = f"termux-tts-speak '{second_inp}'"
            os.system(fout)
            first_inp = second_inp  # Update the input for the next interaction
        else:
            print("AI 2 >> Cleverbot did not respond.")
            break
