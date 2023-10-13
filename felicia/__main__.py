import cleverbotfreeapi
import os
import time

def main():
    user_input = "Hi"  # Initial input from the user
    session = "Deftera"

    while True:
        print("You >> " + user_input)
        user_input_cleaned = user_input.replace("'", '')  # Remove single quotes
        os.system(f"termux-tts-speak '{user_input_cleaned}'")  # Use termux-tts-speak for "You"

        ai_response = cleverbotfreeapi.cleverbot(user_input, session=session)

        if ai_response.strip():  # Check if Cleverbot provided a non-empty response
            ai_response_cleaned = ai_response.replace("'", '')  # Remove single quotes
            print("AI 1 >> " + ai_response_cleaned)
            os.system(f"espeak '{ai_response_cleaned}'")  # Use espeak for "AI 1"
            user_input = ai_response  # Set the response as the next user_input
            time.sleep(5)  # Pause for 5 seconds

        else:
            print("AI 1 >> Cleverbot did not respond.")
            break
