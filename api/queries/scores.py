from pydantic import BaseModel, ValidationError
from typing import Optional, List, Union
from queries.pool import pool
from datetime import datetime
import traceback


class Error(BaseModel):
    message: str


class ScoreIn(BaseModel):
    value: int


class ScoreOut(BaseModel):
    id: str
    user_id: str
    value: int
    created_on: datetime


class ScoreRepository:
    def create_score(self, score: ScoreIn, user_id: int) -> ScoreOut:
        time = datetime.now()
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO scores
                            (user_id, value, created_on)
                        VALUES
                            (%s,%s,%s)
                        RETURNING id;
                        """,
                        [
                            score.value,
                            int(user_id),
                            time,
                        ]
                    )
                    id = str(result.fetchone()[0])
                    return ScoreOut (
                        id=id,
                        user_id=str(user_id),
                        value=score.value,
                        created_on=time
                    )
        except Exception:
            traceback.print_exc()
            return Error(message="Create property failed")
