from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag import awake_rag

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/query/")
async def query_rag(query: Query):
    try:
        print(f"Received query: {query.question}")
        answer = awake_rag(query.question)
        print(f"Sending answer: {answer}")
        return {'answer': answer}
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        return {'error': str(e)}, 500

@app.get("/")
def read_root():
    return {"message": "RAG API is running!"}

@app.get('/favicon.ico', include_in_schema=False)
async def get_favicon():
    return ""