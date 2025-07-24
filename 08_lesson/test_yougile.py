import pytest
import requests

BASE_URL = "https://ru.yougile.com/api-v2/projects"
TOKEN = "GeT2UFh5Uc8ryDK4wEj9iDUecv4chigL-WGMk9Ht1Wa7xnbtkS5UheBTm6dk65Y3"


@pytest.fixture(scope="module")
def headers():
    return {'Authorization': f'Bearer {TOKEN}'}


class TestProjects:

    def test_create_project_success(self, headers):
        data = {"name": "Test Project"}
        response = requests.post(BASE_URL, json=data, headers=headers)
        assert response.status_code == 201
        assert "id" in response.json()

    def test_create_project_failure(self, headers):
        response = requests.post(BASE_URL, json={}, headers=headers)
        assert response.status_code == 400

    def test_get_project_success(self, headers):
        create_response = requests.post(BASE_URL,
                                        json={"name": "Project to Get"},
                                        headers=headers)
        project_id = create_response.json().get('id')

        response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
        assert response.status_code == 200
        assert response.json()['name'] == "Project to Get"

    def test_get_nonexistent_project(self, headers):
        non_existent_id = 9999999  # Пример ID, которого не существует
        response = requests.get(f"{BASE_URL}/{non_existent_id}",
                                headers=headers)
        assert response.status_code == 404

    def test_update_project_success(self, headers):
        create_response = requests.post(BASE_URL,
                                        json={"name": "Project to Update"},
                                        headers=headers)
        project_id = create_response.json().get('id')

        update_data = {"name": "Updated Project Name"}
        response = requests.put(f"{BASE_URL}/{project_id}", json=update_data,
                                headers=headers)
        assert response.status_code == 200
        assert response.json()['name'] == "Updated Project Name"

    def test_update_nonexistent_project(self, headers):
        non_existent_id = 9999999
        update_data = {"name": "Updated Name"}
        response = requests.put(f"{BASE_URL}/{non_existent_id}",
                                json=update_data, headers=headers)
        assert response.status_code == 404
