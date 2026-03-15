from fastapi import APIRouter
from database import SessionLocal
import models
import random

router = APIRouter()


# Get quiz questions
@router.get("/questions")
def get_questions():

    db = SessionLocal()

    questions = db.query(models.Question).all()

    return random.sample(questions, min(len(questions), 5))


# Submit user score
@router.post("/submit")
def submit_score(username: str, score: int):

    db = SessionLocal()

    new_score = models.Score(
        username=username,
        score=score
    )

    db.add(new_score)
    db.commit()

    return {"message": "Score saved successfully"}


# Leaderboard
@router.get("/leaderboard")
def leaderboard():

    db = SessionLocal()

    scores = db.query(models.Score)\
        .order_by(models.Score.score.desc())\
        .limit(10)\
        .all()

    return scores