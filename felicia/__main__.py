import cleverbotfreeapi
import os
import subprocess

def main():
  while True:
    inp = input("You >> ")
    out = cleverbotfreeapi.cleverbot(inp, session="Deftera")
    print("Felicia >>"+out)
    fout = f"termux-tts-speak '{out}'"
    os.system(fout)
