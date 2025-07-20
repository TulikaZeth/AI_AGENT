import os
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from tools.vectorstore_tool import VectorStoreTool


load_dotenv()


folder_path = "data/crop_docs"
docs = []

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        path = os.path.join(folder_path, filename)
        loader = TextLoader(path)
        docs.extend(loader.load())


splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

vstore = VectorStoreTool()
vstore.load_vectorstore(chunks)
