from typing import List, Dict

from app.src.schemas.short_game_result import GameResultInput, GameResultOutput, GameWinType


def calculate_checkers_in_enemy_home(board_points: List[Dict], start_position: int) -> int:
    enemy_home_points_numbers = [i for i in range(0, 6)] if start_position == 23 else [i for i in range(18, 24)]
    result = sum(point.checkers_count for point in board_points if point.number in enemy_home_points_numbers)
    return result


def check_win_type(game_result: GameResultInput) -> GameResultOutput:

    board_points = game_result.board.points

    # Identifying the UUID of the losing player
    for point in board_points:
        if point.occupied_by:
            losing_player_uuid = point.occupied_by
            break

    checkers_on_bar = game_result.board.bar_counts[f'{losing_player_uuid}']
    checkers_in_enemy_home = calculate_checkers_in_enemy_home(
        game_result.board.points,
        game_result.start_position[f'{losing_player_uuid}']
    )
    checkers_in_board = sum(point.checkers_count for point in board_points)

    if checkers_on_bar > 0 or checkers_in_enemy_home > 0:
        response = GameResultOutput(points=3, win_type=GameWinType.Koks)
    elif checkers_in_board < 15:
        response = GameResultOutput(points=1, win_type=GameWinType.Oin)
    else:
        response = GameResultOutput(points=2, win_type=GameWinType.Mars)

    return response
