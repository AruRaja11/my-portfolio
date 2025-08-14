from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag import awake_rag

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],  
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/query/")
async def query_rag(query: Query):
    print(f"Received query: {query.question}")
    answer = awake_rag(query.question)
    print(f"Sending answer: {answer}")
    return {'answer': answer}

@app.get("/")
def read_root():
    return {"message": "RAG API is running!"}