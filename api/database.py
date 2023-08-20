from sqlalchemy import create_engine
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.config import Config


config = Config('.env')


# Sync
SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL')

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Async
# SQLALCHEMY_DATABASE_URL_ASYNC = config('SQLALCHEMY_DATABASE_URL_ASYNC')

# async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL_ASYNC, echo=False)

# async def get_async_db():
#     db = AsyncSession(bind=async_engine, expire_on_commit=False)
#     try:
#         yield db
#     finally:
#         await db.close()