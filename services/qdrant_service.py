# services/qdrant_service.py
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

class QdrantService:
    def __init__(self, collection_name: str, documents: str):
        self.collection_name = collection_name
        self.documents = documents
        self.client = QdrantClient(":memory:")
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        self._create_collection()

    def _create_collection(self):
        # Create a Qdrant collection
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(
                size=self.encoder.get_sentence_embedding_dimension(),
                distance=models.Distance.COSINE,
            ),
        )
        self._upload_documents()

    def _upload_documents(self):
        # Upload documents to Qdrant
        self.client.upload_points(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(
                    id=idx,
                    vector=self.encoder.encode(doc).tolist(),
                    payload={"content": doc}
                )
                for idx, doc in enumerate(self.documents.split('\n\n'))
            ],
        )

    def process_query(self, query_text: str, description: str):
        # Concatenate optional description to query_text
        full_query_text = f"{query_text} {description}".strip()

        # Search for relevant documents
        hits = self.client.search(
            collection_name=self.collection_name,
            query_vector=self.encoder.encode(full_query_text).tolist(),
            limit=3,
        )

        extracted_content = ''
        for hit in hits:
            doc_content = hit.payload["content"]
            if full_query_text in doc_content:
                start = max(doc_content.index(full_query_text) - 100, 0)
                end = min(doc_content.index(full_query_text) + 200, len(doc_content))
                extracted_content += doc_content[start:end] + "\n"

        return hits, extracted_content
