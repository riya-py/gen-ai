from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

loader = TextLoader("document-loaders/notes.txt")
loader = PyPDFLoader("document-loaders/GRU.pdf")
docs = loader.load()

template = ChatPromptTemplate.from_messages([
    ("system","You are an expert text summarizer."),
    ("human","Summarize the following text in 5 bullet points:\n\n{data}")
])
model = ChatMistralAI(model="mistral-small-2506")

prompt = template.format_messages(
    data=docs[0].page_content
)

result = model.invoke(prompt)

print(result.content)