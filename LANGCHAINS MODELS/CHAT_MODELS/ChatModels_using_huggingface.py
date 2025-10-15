from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v0.4",
    task = "text-generation",
)

model = ChatHuggingFace(llm=llm, temperature=0)

result = model.invoke("What is Gen Ai")

print(result.content)