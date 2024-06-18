import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture()
def base_game_result_data():
    return {
        'board': {
            'bar_counts': {
                '1234': 0,
                '5678': 0,
            },
            'points': [{'number': i, 'checkers_count': 0, 'occupied_by': None} for i in range(24)],
        },
        'start_position': {
            '1234': 0,
            '5678': 23,
        }
    }


@pytest.fixture
def koks_data1(base_game_result_data):
    data = base_game_result_data.copy()
    data['board']['bar_counts']['1234'] = 1
    data['board']['points'][0] = {'number': 0, 'checkers_count': 5, 'occupied_by': '1234'}
    data['board']['points'][1] = {'number': 1, 'checkers_count': 3, 'occupied_by': '1234'}
    data['board']['points'][2] = {'number': 2, 'checkers_count': 4, 'occupied_by': '1234'}
    data['board']['points'][3] = {'number': 3, 'checkers_count': 1, 'occupied_by': '1234'}
    data['board']['points'][4] = {'number': 4, 'checkers_count': 1, 'occupied_by': '1234'}
    return data


@pytest.fixture
def koks_data2(base_game_result_data):
    data = base_game_result_data.copy()
    data['board']['points'][0] = {'number': 0, 'checkers_count': 5, 'occupied_by': '1234'}
    data['board']['points'][1] = {'number': 1, 'checkers_count': 3, 'occupied_by': '1234'}
    data['board']['points'][2] = {'number': 2, 'checkers_count': 4, 'occupied_by': '1234'}
    data['board']['points'][3] = {'number': 3, 'checkers_count': 1, 'occupied_by': '1234'}
    data['board']['points'][4] = {'number': 4, 'checkers_count': 1, 'occupied_by': '1234'}
    data['board']['points'][20] = {'number': 20, 'checkers_count': 1, 'occupied_by': '1234'}
    return data


@pytest.fixture
def oin_data(base_game_result_data):
    data = base_game_result_data.copy()
    data['board']['points'][0] = {'number': 0, 'checkers_count': 5, 'occupied_by': '1234'}
    data['board']['points'][1] = {'number': 1, 'checkers_count': 3, 'occupied_by': '1234'}
    data['board']['points'][2] = {'number': 2, 'checkers_count': 4, 'occupied_by': '1234'}
    data['board']['points'][3] = {'number': 3, 'checkers_count': 1, 'occupied_by': '1234'}
    data['board']['points'][4] = {'number': 4, 'checkers_count': 1, 'occupied_by': '1234'}
    return data


@pytest.fixture
def mars_data(base_game_result_data):
    data = base_game_result_data.copy()
    data['board']['points'][0] = {'number': 0, 'checkers_count': 5, 'occupied_by': '1234'}
    data['board']['points'][1] = {'number': 1, 'checkers_count': 3, 'occupied_by': '1234'}
    data['board']['points'][2] = {'number': 2, 'checkers_count': 4, 'occupied_by': '1234'}
    data['board']['points'][3] = {'number': 3, 'checkers_count': 1, 'occupied_by': '1234'}
    data['board']['points'][4] = {'number': 4, 'checkers_count': 1, 'occupied_by': '1234'}
    data['board']['points'][14] = {'number': 14, 'checkers_count': 1, 'occupied_by': '1234'}
    return data
