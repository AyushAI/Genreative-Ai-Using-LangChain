from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-3-5-sonnet-20251022')

result = model.invoke("What is LLM")

print(result.content)