from sqlalchemy import Column, Integer, String
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    option1 = Column(String)
    option2 = Column(String)
    option3 = Column(String)
    option4 = Column(String)
    answer = Column(String)


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    score = Column(Integer)