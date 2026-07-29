from langchain_openai import embeddings, openAIEmbeddings

embeddings = openAIEmbeddings(
    model= 'text-embedding-3-large',
    dimensions=64
)
texts= [
    "hello my name is riya",
    "im studying genai",
    "the person reading this is sweet :)"
]
vector=embeddings.embed_query(texts)
print(vector)