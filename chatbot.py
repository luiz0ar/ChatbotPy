import openai
import speech_recognition as sr
import pyttsx3
import os

key_api=""

openai.api_key = key_api

def talk(texto):
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

r = sr.Recognizer()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)
for indice, vozes in enumerate(voices):
    print(indice, vozes.name)
voz = 1
engine.setProperty('voice', voices[voz].id)


def sendMessage(message, messageList=[]): 
    messageList.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messageList,
    )

    return response.choices[0]["message"]


messageList=[]
while True:
    print("Type your message or type 'exit' to end the conversation.\n")
    text = input("You: ")

    if text == "exit":
        break
    else:
        response = sendMessage(text, messageList)
        messageList.append(response)
        print("Chatbot: ", response["content"])
