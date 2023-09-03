import os
import subprocess
import nltk
import wikipedia

nltk.download("punkt")  # Download NLTK data (if not already downloaded)

from nltk.chat.util import Chat, reflections

def felicia_chatbot():
    print("Hello! I'm Felicia, a female AI chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You >> ")
        response = chat_with_felicia(user_input)
        print("Felicia >>", response)
        os.system(f"termux-tts-speak '{response}'")

def main(input_text):
    if "connect to Wikipedia" in input_text:
        topic = input_text.split("connect to Wikipedia")[1].strip()
        try:
            return wikipedia.summary(topic)
        except wikipedia.exceptions.DisambiguationError as e:
            return wikipedia.summary(e.options[0])
        except wikipedia.exceptions.PageError:
            return "No results found for that topic."
    else:
        return "I can assist you with a wide range of topics. Please specify your question."

if __name__ == "__main__":
    felicia_chatbot()
