import cleverbotfreeapi
import os
import subprocess

def main():
    user_input = "Hi"  # Initial input from the user
    session = "Deftera"
    
    while True:
        print("You >> " + user_input)
        ai_response = cleverbotfreeapi.cleverbot(user_input, session=session)
        
        if ai_response.strip():  # Check if Cleverbot provided a non-empty response
            print("AI 1 >> " + ai_response)
            user_input = ai_response  # User's response is based on AI 1's reply
        else:
            print("AI 1 >> Cleverbot did not respond.")
            break

if __name__ == "__main__":
    main()
