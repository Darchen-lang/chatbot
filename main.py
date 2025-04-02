# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI app instance
app = FastAPI()

# Define the data model for the input
class IdeaInput(BaseModel):
    idea: str  # The input idea

# Create an API endpoint to accept idea inputs
@app.post("/evaluate")
async def evaluate_idea(idea: IdeaInput):
    return {"message": f"Received idea: {idea.idea}"}

# To run this, use 'uvicorn main:app --reload'
