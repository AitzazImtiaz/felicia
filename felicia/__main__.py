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
            os.system(f"espeak '{ai_response}'")  # Use espeak for AI 1's response
            user_input = cleverbotfreeapi.cleverbot(ai_response, session=session)
        else:
            print("AI 1 >> Cleverbot did not respond.")
            break
