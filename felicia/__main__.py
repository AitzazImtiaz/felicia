import cleverbotfreeapi
import os

def main():
    user_input = "Hi"  # Initial input from the user
    session = "Deftera"

    while True:
        print("You >> " + user_input)
        ai_response = cleverbotfreeapi.cleverbot(user_input, session=session)

        if ai_response.strip():  # Check if Cleverbot provided a non-empty response
            print("AI 1 >> " + ai_response)
            user_input = cleverbotfreeapi.cleverbot(ai_response, session=session)
            print("You >> " + user_input)
            fout = f"termux-tts-speak '{user_input}'"
            os.system(fout)
        else:
            print("AI 1 >> Cleverbot did not respond.")
            break
