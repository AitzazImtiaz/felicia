import gpt_2_simple as gpt2
import os

def main():
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, model_name='124M')

    user_input = "Hi"  # Initial input from the user

    while True:
        print("You >> " + user_input)
        ai_response = gpt2.generate(sess, model_name='124M', prefix=user_input, return_as_list=True)[0]

        if ai_response.strip():  # Check if the response is not empty
            print("AI 1 >> " + ai_response)
            os.system(f"espeak '{ai_response}'")  # Use espeak for AI 1's response
            user_input = ai_response
        else:
            print("AI 1 >> AI did not respond.")
            break
