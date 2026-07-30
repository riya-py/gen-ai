from dotenv import load_dotenv
load_dotenv()

# ---------------- Gemini ----------------
from langchain_google_genai import ChatGoogleGenerativeAI

gemini_model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    # temperature=0.7,
    max_tokens=20
)

response1 = gemini_model.invoke("What is cricket?")
print("Gemini:")
print(response1.content)


# ---------------- Groq ----------------
from langchain_groq import ChatGroq

groq_model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=20
)

response2 = groq_model.invoke("What is badminton?")
print("\nGroq:")
print(response2.content)


# ---------------- Mistral ----------------
from langchain_mistralai import ChatMistralAI

mistral_model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.7,
    max_tokens=20
)

response3 = mistral_model.invoke("What is skating?")
print("\nMistral:")
print(response3.content)