import chromadb

from ai.embedding_model import EmbeddingModel


class Retriever:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        self.collection = self.client.get_collection(
            name="telecom_error_codes"
        )

        self.embedding_model = EmbeddingModel()

    def search(self, question, top_k=1):

        query_embedding = self.embedding_model.get_embedding(
            question
        )

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results