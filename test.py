import time
from datetime import datetime

import requests
import pytest

BASE_URL = "http://0.0.0.0:8000"

def test_server_availability():
    url = BASE_URL
    response = requests.get(url)
    assert response.status_code == 200

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
    assert response.json() == {"domains": [
        "sber.ru",
        "stackoverflow.com",
        "ya.ru"
    ]
        , "status": "ok"}

def test_inserted_domains():
    time.sleep(1)
    from_time = int(datetime.now().timestamp())
    url1 = f"{BASE_URL}/visited_links"
    payload = {
        "links": [
            "https://sber.ru/aaa"
        ]
    }
    print(from_time)
    response = requests.post(url1, json=payload)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


    url2 = f"{BASE_URL}/visited_domains"

    to_time = int(datetime.now().timestamp())+1
    params = {"from_time": from_time, "to_time": to_time}
    response2 = requests.get(url2, params=params)


    assert response2.status_code == 200
    assert response2.json() == {"domains": [
        "sber.ru"
    ]
        , "status": "ok"}

if __name__ == "__main__":
    pytest.main([__file__])
