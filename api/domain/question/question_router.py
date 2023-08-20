from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.question import question_schema, question_crud


router = APIRouter(
    prefix="/api/question"
)


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    await question_crud.create_question(db=db, question_create=_question_create)


@router.get("/list", response_model=list[question_schema.Question])
async def question_list(db: Session = Depends(get_db)):
    qustions = await question_crud.get_question_list(db)
    return qustions


@router.get("/detail/{question_id}", response_model=question_schema.Question)
async def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = await question_crud.get_question(db, question_id=question_id)
    return question