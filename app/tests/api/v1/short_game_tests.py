import json

import pytest
from pytest_lazyfixture import lazy_fixture

from app.tests.conftest import client


@pytest.mark.parametrize('input_data, expected_result', [
    (lazy_fixture('koks_data1'), {"points": 3, "win_type": "koks"}),
    (lazy_fixture('koks_data2'), {"points": 3, "win_type": "koks"}),
    (lazy_fixture('oin_data'), {"points": 1, "win_type": "oin"}),
    (lazy_fixture('mars_data'), {'points': 2, 'win_type': 'mars'}),
])
def test_check_win_type_service(input_data, expected_result):
    response = client.post(
        '/api/v1/short-game/check-win-type',
        json=input_data
    )
    response_data = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert response_data == expected_result
