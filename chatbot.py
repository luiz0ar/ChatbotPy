import openai

key_api=""

openai.api_key = key_api

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
