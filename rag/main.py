from langchain_community.document_loaders import ChatPromptTemplate, TextLoader
from langchain_mistralai import ChatMistralAI

loader = TextLoader("notes.txt")
docs = loader.load()

template = ChatPromptTemplate.from_message(
    [("system","You are a ai that summarizes text"),
    ("human","{text}")],
)

model = ChatMistralAI(model="mistral-small-2506")
prompt = template.format_prompt(data=docs[0].page_content)

result = model.invoke(prompt)

print(result)