from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

class RAGRetriever:
    def __init__(self, index_path="data/indexed"):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = FAISS.load_local(
            folder_path=index_path,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

    def retrieve(self, query, k=3):
        docs = self.vectorstore.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]
