from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.7
)
print("--------------------------Welcome type 0 to exit the application----------------------------")
while True:
    prompt=input("you: ")
    if(prompt=="0"):
        break
    response=model.invoke(prompt)

    print("Bot: ",response.content)