import chromadb
from ai.embedding_model import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        # Delete existing collection if present
        try:
            self.client.delete_collection("telecom_error_codes")
            print("Old Vector DB Removed.")
        except:
            pass

        self.collection = self.client.get_or_create_collection(
            name="telecom_error_codes"
        )

        self.embedding_model = EmbeddingModel()

    def build_vector_db(self, error_df):
        """
        Read all error codes and store them in ChromaDB.
        """

        print("\nCreating Vector Database...\n")

        count = 0

        for _, row in error_df.iterrows():

            document = f"""
Error Code : {row['Error_Code']}

Status : {row['Status']}

Category : {row['Category']}

Description :
{row['Description']}

Resolution :
{row['Resolution']}

Severity :
{row['Severity']}

Possible Cause :
{row['Possible_Cause']}
"""

            embedding = self.embedding_model.get_embedding(
                document
            )

            self.collection.add(
                ids=[str(row["Error_Code"])],
                documents=[document],
                embeddings=[embedding]
            )

            count += 1

        print(f"\n✅ {count} Error Codes Stored Successfully.")