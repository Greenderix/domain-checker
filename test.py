import requests
import pytest

BASE_URL = "http://0.0.0.0:8000"


def test_visited_links():
    url = f"{BASE_URL}/visited_links"
    payload = {
        "links": [
            "https://ya.ru/",
            "https://ya.ru/search/?text=мемы+с+котиками",
            "https://sber.ru",
            "https://stackoverflow.com/questions/65724760/how-it-is"
        ]
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_visited_domains():
    url = f"{BASE_URL}/visited_domains"
    from_time = 1545221231
    to_time = 1545255555

    params = {"from_time": from_time, "to_time": to_time}
    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.json() == {"domains": ["sber.ru",
    "stackoverflow.com",
    "ya.ru"], "status": "ok"}


if __name__ == "__main__":
    pytest.main([__file__])
