from flask.testing import FlaskClient
import datetime


def get_moscow_time():
    timezone_info = datetime.timezone(datetime.timedelta(hours=+3))
    current_time = datetime.datetime.now(timezone_info)
    return current_time.strftime("%H:%M:%S")


def test_correct_time(client: FlaskClient):
    res = client.get("/")
    assert res.status_code == 200

    expected_time = get_moscow_time()
    assert expected_time in res.data
