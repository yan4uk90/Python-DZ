import pytest
import requests

BASE_URL = "https://ru.yougile.com/api-v2/projects"
TOKEN = "GeT2UFh5Uc8ryDK4wEj9iDUecv4chigL-WGMk9Ht1Wa7xnbtkS5UheBTm6dk65Y3"


@pytest.fixture
def create_project():
    return test_create_new_project_pozitive()


def test_create_new_project_pozitive():
    payload = """{
        "title": "new progect"
        "users": {"cf8a8951-ccfd-4d55-a9e4-8e35af5be22d": "worker"}
        }
"""
    headers = """{
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}
        }
"""
    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 201
    respons_data = response.json()
    project_id = respons_data[id]
    return project_id


# пустое поле title
def test_create_new_project_negative():
    payload = """{
        "title": ""
        "users": {"cf8a8951-ccfd-4d55-a9e4-8e35af5be22d": "worker"}
        }
"""
    headers = """{
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}
        }
"""
    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 400


def test_editing_project_pozitive(create_projec):
    progect_id = create_project
    payload = """{
        "deleted": False,
        "title": "ГосУслуги"
        "users": {"cf8a8951-ccfd-4d55-a9e4-8e35af5be22d": "worker"}
        }
"""
    headers = """{
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}
        }
"""
    response = requests.put(f"{BASE_URL}/{progect_id}", json=payload,
                            headers=headers)
    assert response.status_code == 200


# Неверное id
id_negative = "12131225514432"


def test_editing_project_negative():
    payload = """{
        "deleted": False,
        "title": "ГосУслуги"
        "users": {"cf8a8951-ccfd-4d55-a9e4-8e35af5be22d": "worker"}
        }
"""
    headers = """{
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}
        }
"""
    response = requests.put(f"{BASE_URL}/{id_negative}", json=payload,
                            headers=headers)
    assert response.status_code == 404


def test_get_by_id_pozitive(create_projec):
    progect_id = create_project
    headers = """{
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}
        }
"""
    response = requests.get(f"{BASE_URL}/{progect_id}", headers=headers)
    assert response.status_code == 200


def test_get_by_id_negative():
    headers = """{
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}
        }
"""
    response = requests.get(f"{BASE_URL}/{id_negative}", headers=headers)
    assert response.status_code == 404
