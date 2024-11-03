from fastapi import FastAPI
from pydantic import BaseModel
from . import EmbeddingModel

class EmbedRequest(BaseModel):
    paragraph: str

app = FastAPI()
model = EmbeddingModel()

@app.post("/embed") 
def embed(request: EmbedRequest):
  embeddings = model.embed([request.paragraph])
  return {"embeddings": embeddings[0]}

@app.get("/health")
def health_check():
    return {"status": "healthy"}