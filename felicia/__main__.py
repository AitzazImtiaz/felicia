import os
import subprocess
import nltk
import wikipedia  # For connecting to Wikipedia

nltk.download("punkt")  # Download NLTK data (if not already downloaded)

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?",]
    ],
    [
        r"what is your name?",
        ["I'm Felicia, a female AI chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, so I don't have feelings, but I'm here to help you.",]
    ],
    [
        r"(.*) (weather|temperature) in (.*)",
        ["I'm sorry, I cannot provide real-time weather information.",]
    ],
    [
        r"(.*) help (.*)",
        ["I can assist you with a wide range of topics. Please specify your question.",]
    ],
    [
        r"(.*) your name?",
        ["I told you, I'm Felicia, a female AI chatbot.",]
    ],
    [
        r"(.*) (connect|search) to Wikipedia (.*)",
        [wikipedia.summary("%3"),]
    ],
    [
        r"quit",
        ["Goodbye! If you have more questions, feel free to ask later.",]
    ],
]

def main():
    print("Hello! I'm Felicia, a female AI chatbot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You >> ")
        response = chat.respond(user_input)
        print("Felicia >>", response)
        os.system(f"termux-tts-speak '{response}'")
