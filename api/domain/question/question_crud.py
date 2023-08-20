from datetime import datetime
from sqlalchemy.orm import Session

from domain.question.question_schema import QuestionCreate
from models import Question


async def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now())
    db.add(db_question)
    db.commit()


async def get_question_list(db: Session):
    qustion_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return qustion_list


async def get_question(db: Session, question_id: int):
    question = db.get(Question, question_id)
    return question