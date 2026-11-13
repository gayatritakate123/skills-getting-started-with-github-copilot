from fastapi.testclient import TestClient

from src import app as app_module


client = TestClient(app_module.app)


def test_get_cities_for_country(monkeypatch):
    request = {}

    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return {"error": False, "data": ["Toronto", "Vancouver"]}

    def fake_post(url, json, timeout):
        request.update(url=url, json=json, timeout=timeout)
        return Response()

    monkeypatch.setattr(app_module.httpx, "post", fake_post)

    response = client.get("/countries/Canada/cities")

    assert response.status_code == 200
    assert response.json() == {
        "country": "Canada",
        "region": None,
        "cities": ["Toronto", "Vancouver"],
    }
    assert request["url"].endswith("/countries/cities")
    assert request["json"] == {"country": "Canada"}


def test_get_cities_for_spain(monkeypatch):
    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return {"error": False, "data": ["Madrid", "Barcelona", "Valencia"]}

    monkeypatch.setattr(
        app_module.httpx,
        "post",
        lambda *args, **kwargs: Response(),
    )

    response = client.get("/countries/Spain/cities")

    assert response.status_code == 200
    assert response.json() == {
        "country": "Spain",
        "region": None,
        "cities": ["Madrid", "Barcelona", "Valencia"],
    }


def test_get_cities_for_region(monkeypatch):
    request = {}

    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return {"error": False, "data": ["Montreal", "Quebec City"]}

    def fake_post(url, json, timeout):
        request.update(url=url, json=json, timeout=timeout)
        return Response()

    monkeypatch.setattr(app_module.httpx, "post", fake_post)

    response = client.get("/countries/Canada/cities?region=Quebec")

    assert response.status_code == 200
    assert response.json()["cities"] == ["Montreal", "Quebec City"]
    assert response.json()["region"] == "Quebec"
    assert request["url"].endswith("/countries/state/cities")
    assert request["json"] == {"country": "Canada", "state": "Quebec"}


def test_get_cities_returns_not_found_for_unknown_location(monkeypatch):
    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return {"error": True, "msg": "Country not found"}

    monkeypatch.setattr(app_module.httpx, "post", lambda *args, **kwargs: Response())

    response = client.get("/countries/Nowhere/cities")

    assert response.status_code == 404
    assert response.json()["detail"] == "Country not found"