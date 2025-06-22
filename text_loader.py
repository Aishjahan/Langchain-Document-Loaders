from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

template = PromptTemplate(
    template='Generate a summary of {text}',
    input_variables=['text']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(docs)
print(type(docs))
print(len(docs))
print(docs[0])

print(docs[0].metadata)

chain = template | model | parser

print(chain.invoke({'text' : docs[0].page_content}))