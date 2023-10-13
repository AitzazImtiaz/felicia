import os
import cleverbotfreeapi

def main():
    user_input = "Hi"  # Initial input from the user
    session = "Deftera"
    
    proxy_index = 0  # Start with the first proxy

    while True:
        print("You >> " + user_input)

        # Use the current proxy for the request using proxychains
        proxy_command = f"proxychains4 -q cleverbotfreeapi.cleverbot -s '{session}' '{user_input}'"
        ai_response = os.popen(proxy_command).read()

        if ai_response.strip():  # Check if Cleverbot provided a non-empty response
            print("AI 1 >> " + ai_response)
            os.system(f"espeak '{ai_response}'")  # Use espeak for AI 1's response
            user_input = ai_response
        else:
            print("AI 1 >> Cleverbot did not respond.")
            break

        # Rotate to the next proxy or loop back to the first one
        proxy_index = (proxy_index + 1) % len(proxies)
