from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.9
)
print("--------------------------Welcome type 0 to exit the application----------------------------")

print("choose your ai mode")
print("press 1 for sad ai chatbot")
print("press 2 for funny ai chatbot")
print("press 3 for angry ai chatbot")

choice=int(input("enter your choice: "))

if choice == 1:
    messages=[
        SystemMessage(content="You are a sad AI assistant.")
    ]
elif choice == 2:
    messages=[
        SystemMessage(content="You are a funny AI assistant.")
    ]
elif choice == 3:
    messages=[
        SystemMessage(content="You are an angry AI assistant.")
    ]
else:
    print("Invalid choice. Exiting...")
    exit()

while True:
    prompt=input("you: ")
    messages.append(HumanMessage(content=prompt))
    if(prompt=="0"):
        break
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: ",response.content)

print(messages)   # prints the message