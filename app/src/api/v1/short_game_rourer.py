from fastapi import APIRouter

from app.src.schemas.short_game_result import GameResultInput, GameResultOutput
from app.src.services.short_game import check_win_type


router = APIRouter()


@router.post("/check-win-type", status_code=200)
def check_win_type_service(game_result: GameResultInput) -> GameResultOutput:
    return check_win_type(game_result)


