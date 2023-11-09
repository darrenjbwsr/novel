import os
from fastapi import APIRouter, Depends
from typing import List
from authenticator import AccountAuthenticator
from queries.scores import (
    ScoreRepository,
    ScoreIn,
    ScoreOut
)

authenticator = AccountAuthenticator(os.environ["SIGNING_KEY"])
router = APIRouter()

@router.post("/create/score/", response_model=ScoreOut)
def create_score(
    score: ScoreIn,
    repo: ScoreRepository = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    user_id = account_data["id"]
    return repo.create_score(score, int(user_id))
