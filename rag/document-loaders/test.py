from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

splitter=CharacterTextSplitter(
    separator="",
    chunk_size=10, 
    chunk_overlap=1)

loader = TextLoader("notes.txt")
docs = loader.load()
splits = splitter.split_documents(docs)

for i in splits:
    print(i.page_content)
    print("----")
    print("")
