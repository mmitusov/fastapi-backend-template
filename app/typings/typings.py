from pydantic import BaseModel

class Type(BaseModel):
    question: str
    repo_name: str