import cleverbotfreeapi
import os
import time

def main():
    user_input = "Hi"  # Initial input from the user
    session = "Deftera"

    while True:
        user_input_cleaned = user_input.replace("'", "")
        print("You >> " + user_input)
        os.system(f"termux-tts-speak '{user_input_cleaned}'")  # Use espeak for AI 1's response
        ai_response = cleverbotfreeapi.cleverbot(user_input, session=session)
        time.sleep(2.5)
        if ai_response.strip():  # Check if Cleverbot provided a non-empty response
            ai_response_cleaned = ai_response.replace("'", "")
            print("AI 1 >> " + ai_response)
            os.system(f"espeak '{ai_response_cleaned}'")  # Use espeak for AI 1's response
            user_input = cleverbotfreeapi.cleverbot(ai_response, session=session)
        else:
            print("AI 1 >> Cleverbot did not respond.")
            break
        time.sleep(2.5)
