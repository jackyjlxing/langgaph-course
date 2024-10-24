from langchain import hub
from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

# llm = ChatOpenAI(temperature=0)
llm = ChatOllama(temperature=0, model="llama3.2")
prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()
