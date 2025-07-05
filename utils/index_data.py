import os
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

def load_raw_documents(folder='data/raw'):
    texts = []
    for file in os.listdir(folder):
        if file.endswith('.txt'):
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                texts.append(f.read())
    return texts

def index_documents():
    load_dotenv()
    texts = load_raw_documents()
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_texts(texts, embeddings)
    vectordb.save_local("data/indexed")
    print("✅ Indexing complete! Vector store saved.")

if __name__ == "__main__":
    index_documents()
