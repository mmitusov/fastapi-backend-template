from fastapi import APIRouter
from app.controllers.controller import Controller
from app.typings.typings import Type

router = APIRouter()

@router.get('/')
async def root():
    return {"Api": "working correctly!"}
  
@router.post('/test1')
async def update_db():
    data = await Controller.method1()
    return {"Message": data}

@router.post('/test2')
async def answer_questions(question_obj: Type):
    question = question_obj.question
    repo_name = question_obj.repo_name
    data = await Controller.method2(question, repo_name)
    return data