from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts= [
    "hello my name is riya",
    "im learning genai",
    "the person reading this is sweet :)"
]

vector=embeddings.embed_documents(texts)

print(vector)

