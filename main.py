# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI app instance
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://127.0.0.1:5500"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data model for the input
class IdeaInput(BaseModel):
    idea: str  # The input idea

# Create an API endpoint to accept idea inputs
@app.post("/evaluate")
async def evaluate_idea(idea: IdeaInput):
    return {"message": f"Received idea: {idea.idea}"}

# To run this, use 'uvicorn main:app --reload'
