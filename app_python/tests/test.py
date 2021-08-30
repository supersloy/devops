import datetime
from flask.testing import FlaskClient


def get_moscow_time():
    timezone_info = datetime.timezone(datetime.timedelta(hours=+3))
    current_time = datetime.datetime.now(timezone_info)
    return current_time.strftime("%H:%M:%S")


def test_status_code(client: FlaskClient):
    endpoints = ["/", "/api/time"]
    for endpoint in endpoints:
        assert client.get(endpoint).status_code == 200


def test_correct_time_main_page(client: FlaskClient):
    res = client.get("/")

    expected_time = get_moscow_time()
    assert expected_time in res.data.decode('ascii')


def test_correct_time_data(client: FlaskClient):
    res = client.get("/api/time")

    expected_time = get_moscow_time()
    assert expected_time == res.data.decode('ascii')
