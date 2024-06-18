from fastapi import FastAPI
from app.src.api.v1.short_game_rourer import router as game_router_v1

app = FastAPI()


app.include_router(
    game_router_v1,
    prefix="/api/v1/short-game",
    tags=["game"]
)
