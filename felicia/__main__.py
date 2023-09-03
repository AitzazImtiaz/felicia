from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import wikipedia

# Create a chatbot instance
chatbot = ChatBot('Felicia')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

def main():
    print("Hello! I'm Felicia, your friendly chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You >> ")
        if user_input.lower() == "quit":
            print("Felicia >> Goodbye! Have a great day!")
            break
        elif "search Wikipedia" in user_input:
            topic = user_input.split("search Wikipedia")[1].strip()
            response = get_wikipedia_summary(topic)
        else:
            response = chatbot.get_response(user_input)
            
        print("Felicia >>", response)
        
        # Use Termux TTS to speak the response
        os.system(f"termux-tts-speak '{response}'")

def get_wikipedia_summary(topic):
    try:
        summary = wikipedia.summary(topic)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "Wikipedia Disambiguation: " + str(e.options)
    except wikipedia.exceptions.PageError:
        return "No results found for that Wikipedia topic."
