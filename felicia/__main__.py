import cleverbotfreeapi
import os
import subprocess

def main():
  while True:
    inp = subprocess.getoutput("termux-speech-to-text")
    print("You >> "+inp)
    out = cleverbotfreeapi.cleverbot(inp, session="Deftera")
    print("Felicia >>"+out)
    fout = f"termux-tts-speak '{out}'"
    os.system(fout)
