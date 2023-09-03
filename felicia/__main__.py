import os
import subprocess
from chatbot import Chat, register_call
import wikipedia


@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query

def main():
  while True:
    inp = input("You >> ")
    out = Chat("examples/Example.template").converse(inp)
    print("Felicia >>"+out)
    fout = f"termux-tts-speak '{out}'"
    os.system(fout)
