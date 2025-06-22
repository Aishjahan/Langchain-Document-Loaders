from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.in/gp/buyagain/ref=pd_hp_d_atf_rp_1?ie=UTF8&ats=eyJleHBsaWNpdENhbmRpZGF0ZXMiOiJCMDgyTkw0U05QIiwiY3VzdG9tZXJJZCI6IkExQkFFSVJHWTVNOVROIn0%3D&pd_rd_w=61SWI&content-id=amzn1.sym.c4a419ec-0102-4c67-84be-bc36cd160d54&pf_rd_p=c4a419ec-0102-4c67-84be-bc36cd160d54&pf_rd_r=XE6NKMV1BSYFDVG52FGD&pd_rd_wg=UPC0m&pd_rd_r=d0187c2e-b08a-4d5e-8848-b60285379c61'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))