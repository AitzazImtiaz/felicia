import os
import subprocess
import nltk
import wikipedia

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
        [lambda matches: wikipedia_summary(matches[2]) if wikipedia.search(matches[2]) else "No results found.",]
    ],
    [
        r"quit",
        ["Goodbye! If you have more questions, feel free to ask later.",]
    ],
]

def wikipedia_summary(topic):
    try:
        return wikipedia.summary(topic)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0])
    except wikipedia.exceptions.PageError:
        return "No results found for that topic."

def main():
    print("Hello! I'm Felicia, a female AI chatbot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You >> ")
        response = chat.respond(user_input)
        print("Felicia >>", response)
        os.system(f"termux-tts-speak '{response}'")

