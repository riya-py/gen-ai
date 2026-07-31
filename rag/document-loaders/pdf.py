from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

data = PyPDFLoader("GRU.pdf")

docs=data.load()

print(docs[14])