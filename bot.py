import os

from groq import Groq

client = Groq(
    api_key= "gsk_Enter ur API KEY",)


def chat(prompt): 
    chat_completion = client.chat.completions.create(
        messages=[ { "role": "user", "content": prompt,}],
        model="llama3-70b-8192",
    )
    return(chat_completion.choices[0].message.content)

# print(chat("How to import from python file  to  a different file in same folder "))
