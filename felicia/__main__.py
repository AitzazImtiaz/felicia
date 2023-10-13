import cleverbotfreeapi
import os
import time

def main():
    user_input = "Hi"  # Initial input from the user
    session = "Deftera"

    while True:
        print("You >> " + user_input)
        os.system(f"termux-tts-speak '{user_input}'")  # Use espeak for AI 1's response
        ai_response = cleverbotfreeapi.cleverbot(user_input, session=session)
        time.sleep(2.5)
        if ai_response.strip():  # Check if Cleverbot provided a non-empty response
            print("AI 1 >> " + ai_response)
            os.system(f"espeak '{ai_response}'")  # Use espeak for AI 1's response
            user_input = cleverbotfreeapi.cleverbot(ai_response, session=session)
        else:
            print("AI 1 >> Cleverbot did not respond.")
            break
        time.sleep(2.5)
