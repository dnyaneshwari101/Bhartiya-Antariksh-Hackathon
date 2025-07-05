from modules.rag_retriever import RAGRetriever
retriever = RAGRetriever()
query = "Which districts in Punjab are flood-prone?"
results = retriever.retrieve(query)
print("\n📄 Retrieved Results:\n")
for i, doc in enumerate(results, 1):
    print(f"{i}. {doc}\n")
