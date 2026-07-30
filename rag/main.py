from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

loader = TextLoader("notes.txt")
docs = loader.load()

template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that summarizes text."),
    ("human", "{text}")
])

model = ChatMistralAI(model="mistral-small-2506")

prompt = template.invoke({
    "text": docs[0].page_content
})

result = model.invoke(prompt)

print(result.content)