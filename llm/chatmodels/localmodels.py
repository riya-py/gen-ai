from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.7,
        "repetition_penalty": 1.2,
    },
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("What is data?")
print(response.content)