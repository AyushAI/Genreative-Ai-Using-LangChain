from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')

result = model.invoke("Explain ML to a child in easy and fun way")

print(result.content)

