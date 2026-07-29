from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.7
)

messages=[

]

print("--------------------------Welcome type 0 to exit the application----------------------------")
while True:
    prompt=input("you: ")
    messages.append(prompt)
    if(prompt=="0"):
        break
    response=model.invoke(prompt)
    messages.append(response.content)
    print("Bot: ",response.content)

print(messages)   # prints the message