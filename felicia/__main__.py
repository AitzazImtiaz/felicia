import cleverbotfreeapi
import os
import time

def main():
    session = "Deftera"
    user_input = "Hi"  # Initial input from the user

    while True:
        print("You >> " + user_input)
        time.sleep(2.5)
        # Use the current user input as input for Cleverbot
        ai_response = cleverbotfreeapi.cleverbot(user_input, session=session)

        if ai_response.strip():  # Check if Cleverbot provided a non-empty response
            ai_response_cleaned = ai_response.replace("'", '')  # Remove single quotes
            print("AI 1 >> " + ai_response_cleaned)
            os.system(f"espeak '{ai_response_cleaned}'")  # Use espeak for "AI 1"
        else:
            print("AI 1 >> Cleverbot did not respond.")
            break

        user_input = ai_response  # Set the response as the next user input
        user_input_cleaned = user_input.replace("'", '')  # Remove single quotes
        os.system(f"termux-tts-speak '{user_input_cleaned}'")  # Use termux-tts-speak for "You"

        time.sleep(2.5)  # Pause for 5 seconds
