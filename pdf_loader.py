from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('cloud_computing.pdf')

docs = loader.load()

print(docs)

print(len(docs))

print(docs[0].metadata)