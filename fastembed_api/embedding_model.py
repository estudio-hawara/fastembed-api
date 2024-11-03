from fastembed import TextEmbedding
from typing import List

class EmbeddingModel:
    def __init__(self, model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"):
        self.model = TextEmbedding(model_name=model_name)

    def embed(self, documents: List[str]) -> List[float]:
        embeddings = self.model.embed(documents)
        return [e.tolist() for e in embeddings]
