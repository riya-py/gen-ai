from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

data = WebBaseLoader("https://www.apple.com/in/macbook-pro/")

docs=data.load()

print(docs[0].content)