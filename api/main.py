from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.question import question_router
from domain.answer import answer_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(question_router.router)
app.include_router(answer_router.router)